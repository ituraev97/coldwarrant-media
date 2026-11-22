#!/usr/bin/env python3
"""Upload a file to the owner's Google Drive (app "SWR uploader", scope drive.file) and print its Drive link.

Credentials: env DRIVE_CLIENT_ID, DRIVE_CLIENT_SECRET, DRIVE_REFRESH_TOKEN, or a JSON file passed with --creds
(keys client_id, client_secret, refresh_token). Values live in the project doc claude/google-drive-oauth.md;
never commit them to a git repository.

Usage:
  drive_upload.py FILE [--folder "Still Window Rain"] [--creds creds.json] [--delete FILE_ID]
Prints JSON: {"id", "name", "size", "link"}. Pass "link" to Metricool as media; Metricool fetches it through
the owner's linked Google Drive. Old uploads can be removed with --delete <id> (the app may only touch files
it created itself).

Hosts used: www.googleapis.com only (token refresh via /oauth2/v4/token, because oauth2.googleapis.com is not
reachable from the cloud sandbox).
"""
import argparse, json, os, sys, urllib.parse, urllib.request

API = "https://www.googleapis.com"


def creds(path):
    if path:
        c = json.load(open(path))
        return c["client_id"], c["client_secret"], c["refresh_token"]
    return os.environ["DRIVE_CLIENT_ID"], os.environ["DRIVE_CLIENT_SECRET"], os.environ["DRIVE_REFRESH_TOKEN"]


def access_token(cid, secret, refresh):
    data = urllib.parse.urlencode(dict(client_id=cid, client_secret=secret, refresh_token=refresh,
                                       grant_type="refresh_token")).encode()
    with urllib.request.urlopen(urllib.request.Request(API + "/oauth2/v4/token", data=data), timeout=30) as r:
        return json.load(r)["access_token"]


def req(method, url, tok, body=None, headers=None):
    h = {"Authorization": "Bearer " + tok}
    h.update(headers or {})
    r = urllib.request.Request(url, data=body, method=method, headers=h)
    return urllib.request.urlopen(r, timeout=600)


def folder_id(tok, name):
    q = urllib.parse.quote(f"name = '{name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false")
    with req("GET", f"{API}/drive/v3/files?q={q}&fields=files(id)", tok) as r:
        files = json.load(r)["files"]
    if files:
        return files[0]["id"]
    body = json.dumps({"name": name, "mimeType": "application/vnd.google-apps.folder"}).encode()
    with req("POST", f"{API}/drive/v3/files?fields=id", tok, body, {"Content-Type": "application/json"}) as r:
        return json.load(r)["id"]


def upload(tok, path, parent):
    name = os.path.basename(path)
    size = os.path.getsize(path)
    mime = {"mp4": "video/mp4", "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png"}.get(
        name.lower().rsplit(".", 1)[-1], "application/octet-stream")
    meta = json.dumps({"name": name, "parents": [parent]}).encode()
    with req("POST", f"{API}/upload/drive/v3/files?uploadType=resumable", tok, meta,
             {"Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": mime,
              "X-Upload-Content-Length": str(size)}) as r:
        session = r.headers["Location"]
    chunk = 32 * 1024 * 1024  # multiple of 256 KiB
    sent = 0
    with open(path, "rb") as f:
        while sent < size:
            data = f.read(chunk)
            end = sent + len(data) - 1
            try:
                with req("PUT", session, tok, data, {"Content-Length": str(len(data)),
                                                       "Content-Range": f"bytes {sent}-{end}/{size}"}) as r:
                    res = json.load(r)
                    sent = size
            except urllib.error.HTTPError as e:
                if e.code != 308:  # 308 = chunk accepted, continue
                    raise
                sent = end + 1
                print(f"uploaded {sent / size:.0%}", file=sys.stderr)
    return res["id"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--folder", default="Still Window Rain")
    ap.add_argument("--creds")
    ap.add_argument("--delete")
    ap.add_argument("--cleanup-days", type=float, help="delete this app's files in --folder older than N days")
    ap.add_argument("--share", help="make an already uploaded file id viewable by link and print its direct URL")
    a = ap.parse_args()
    tok = access_token(*creds(a.creds))
    if a.cleanup_days is not None:
        import datetime
        fid_ = folder_id(tok, a.folder)
        cutoff = (datetime.datetime.utcnow() - datetime.timedelta(days=a.cleanup_days)).strftime("%Y-%m-%dT%H:%M:%S")
        q = urllib.parse.quote(f"'{fid_}' in parents and trashed = false and createdTime < '{cutoff}'")
        with req("GET", f"{API}/drive/v3/files?q={q}&fields=files(id,name,createdTime)&pageSize=200", tok) as r:
            old = json.load(r)["files"]
        for f in old:
            req("DELETE", f"{API}/drive/v3/files/{f['id']}", tok).close()
        print(json.dumps({"deleted": [f["name"] for f in old]}))
        return
    if a.delete:
        req("DELETE", f"{API}/drive/v3/files/{a.delete}", tok).close()
        print(json.dumps({"deleted": a.delete}))
        return
    if a.share:
        share(tok, a.share)
        print(json.dumps({"id": a.share, "direct": direct(a.share)}))
        return
    fid = upload(tok, a.file, folder_id(tok, a.folder))
    share(tok, fid)
    print(json.dumps({"id": fid, "name": os.path.basename(a.file), "size": os.path.getsize(a.file),
                      "link": f"https://drive.google.com/file/d/{fid}/view", "direct": direct(fid)}))


def share(tok, fid):
    """Anyone with the link can view (Metricool downloads media as an anonymous client)."""
    body = json.dumps({"role": "reader", "type": "anyone"}).encode()
    req("POST", f"{API}/drive/v3/files/{fid}/permissions", tok, body, {"Content-Type": "application/json"}).close()


def direct(fid):
    # direct download URL that skips Drive's virus-scan page for large files
    return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"


if __name__ == "__main__":
    main()
