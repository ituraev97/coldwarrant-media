#!/usr/bin/env python3
"""Real-footage client for the cloud YouTube tasks (cloud side). The cloud sandbox cannot reach youtube.com, so a relay on
the owner's server downloads clips and hands them over through Google Drive folder "FOOTAGE RELAY" (--folder to override).

  python3 footage_client.py request RUN clips.json --creds /tmp/drive_creds.json   # clips.json: [{"name","src","start","end"}]
  python3 footage_client.py wait RUN OUTDIR --creds /tmp/drive_creds.json [--timeout 1800]
`src` = YouTube video id or any yt-dlp URL (archive.org, C-SPAN, ...). start/end "M:SS" (≤ 90 s per clip, ≤ 40 clips).
`wait` polls every 30 s until done_RUN.json appears, downloads every clip to OUTDIR/<name>.mp4 and prints the manifest.
Only the Python standard library is used.
"""
import argparse, json, os, sys, time, urllib.parse, urllib.request

API = "https://www.googleapis.com"
FOLDER = "FOOTAGE RELAY"

def token(path):
    c = json.load(open(path))
    body = urllib.parse.urlencode({"client_id": c["client_id"], "client_secret": c["client_secret"],
                                   "refresh_token": c["refresh_token"], "grant_type": "refresh_token"}).encode()
    with urllib.request.urlopen("https://www.googleapis.com/oauth2/v4/token", body, timeout=60) as r:
        return json.load(r)["access_token"]

def req(method, url, tok, body=None, headers=None):
    h = {"Authorization": "Bearer " + tok}; h.update(headers or {})
    return urllib.request.urlopen(urllib.request.Request(url, data=body, method=method, headers=h), timeout=900)

def folder(tok, FOLDER):
    q = urllib.parse.quote(f"name = '{FOLDER}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false")
    with req("GET", f"{API}/drive/v3/files?q={q}&fields=files(id)", tok) as r:
        f = json.load(r)["files"]
    if f:
        return f[0]["id"]
    b = json.dumps({"name": FOLDER, "mimeType": "application/vnd.google-apps.folder"}).encode()
    with req("POST", f"{API}/drive/v3/files?fields=id", tok, b, {"Content-Type": "application/json"}) as r:
        return json.load(r)["id"]

def find(tok, parent, name):
    q = urllib.parse.quote(f"'{parent}' in parents and name = '{name}' and trashed = false")
    with req("GET", f"{API}/drive/v3/files?q={q}&fields=files(id)", tok) as r:
        f = json.load(r)["files"]
    return f[0]["id"] if f else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["request", "wait"]); ap.add_argument("run"); ap.add_argument("arg")
    ap.add_argument("--creds", default="/tmp/drive_creds.json"); ap.add_argument("--folder", default=FOLDER); ap.add_argument("--timeout", type=int, default=1800)
    a = ap.parse_args()
    tok = token(a.creds); parent = folder(tok, a.folder)
    if a.cmd == "request":
        clips = json.load(open(a.arg))
        data = json.dumps({"run": a.run, "clips": clips}).encode()
        meta = json.dumps({"name": f"req_{a.run}.json", "parents": [parent]}).encode()
        with req("POST", f"{API}/upload/drive/v3/files?uploadType=resumable", tok, meta,
                 {"Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": "application/json"}) as r:
            loc = r.headers["Location"]
        with req("PUT", loc, tok, data, {"Content-Type": "application/json"}) as r:
            print(json.dumps({"requested": len(clips), "file": json.load(r)["id"]}))
        return
    os.makedirs(a.arg, exist_ok=True)
    t0 = time.time()
    while True:
        fid = find(tok, parent, f"done_{a.run}.json")
        if fid:
            break
        if time.time() - t0 > a.timeout:
            sys.exit("timeout: relay did not answer (server offline?) — continue without real footage")
        time.sleep(30)
        if time.time() - t0 > 3000:
            tok = token(a.creds)
    with req("GET", f"{API}/drive/v3/files/{fid}?alt=media", tok) as r:
        done = json.load(r)
    for name, info in done["clips"].items():
        if "id" in info:
            with req("GET", f"{API}/drive/v3/files/{info['id']}?alt=media", tok) as r, open(f"{a.arg}/{name}.mp4", "wb") as f:
                f.write(r.read())
    print(json.dumps(done, indent=1))

if __name__ == "__main__":
    main()
