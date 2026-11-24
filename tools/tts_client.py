#!/usr/bin/env python3
"""Chatterbox voice (natural male narrator) via the owner's server (Drive folder "TTS RELAY"). Standard library only.
Used by SWORN, COLD WARRANT and other cloud channels.

  python3 tts_client.py request-spec RUN spec.json --creds /tmp/drive_creds.json [--hint "..."]
      Generic form. spec.json = {"<out_dir_key>": {"lines": ["text", ...], "names": ["raw_01.wav", ...], "tempo": 1.0,
      "speed": 1.0}, ...}. Every line becomes <out_dir_key>/<name> (48 kHz mono wav) in the result zip.
      "tempos": [per-line factors] optional. "tempo" = speed-up factor applied after synthesis (1.0 = natural pace = MAX for long-form, owner 2026-11-24; Shorts ≤ 1.10 — the relay clamps higher values).

  python3 tts_client.py request RUN EPISODE_DIR --creds /tmp/drive_creds.json [--hint "Names, Companies"]
      Builds the request from EPISODE_DIR/episode.json (key "vo", speed 0.98) and every short*.json (key "s<N>/vo", speed 1.15)
      — the same keys/speeds pipeline/make.sh passes to tts.py — and uploads req_RUN.json. Voicing takes ~4–6 h on the server.
  python3 tts_client.py status RUN --creds ...          -> prints {"state": "missing|pending|ready|failed", ...}
  python3 tts_client.py fetch RUN WORKDIR --creds ...   -> unzips vo_RUN.zip into WORKDIR (WORKDIR/vo, WORKDIR/s1/vo, ...)
      Then run make.sh with the same WORKDIR: tts.py finds matching cache.json keys and keeps the Chatterbox audio.
      Any line whose text changed after the request is re-voiced by Kokoro (mixed voices!) — do not edit text after requesting.
"""
import argparse, glob, io, json, os, re, sys, urllib.parse, urllib.request, zipfile

API = "https://www.googleapis.com"
FOLDER = "TTS RELAY"

def token(path):
    c = json.load(open(path))
    body = urllib.parse.urlencode({"client_id": c["client_id"], "client_secret": c["client_secret"],
                                   "refresh_token": c["refresh_token"], "grant_type": "refresh_token"}).encode()
    with urllib.request.urlopen("https://www.googleapis.com/oauth2/v4/token", body, timeout=60) as r:
        return json.load(r)["access_token"]

def req(method, url, tok, body=None, headers=None):
    h = {"Authorization": "Bearer " + tok}; h.update(headers or {})
    return urllib.request.urlopen(urllib.request.Request(url, data=body, method=method, headers=h), timeout=900)

def folder(tok):
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

def get(tok, fid):
    with req("GET", f"{API}/drive/v3/files/{fid}?alt=media", tok) as r:
        return r.read()

def build(ep):
    specs = {"vo": {"speed": 0.98, "lines": [l.get("say", "") for l in json.load(open(f"{ep}/episode.json"))["lines"]]}}
    for f in sorted(glob.glob(f"{ep}/short*.json")):
        n = re.sub(r"\D", "", os.path.basename(f))
        if not n:
            continue
        specs[f"s{n}/vo"] = {"speed": 1.15, "lines": [l.get("say", "") for l in json.load(open(f))["lines"]]}
    return specs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["request", "request-spec", "status", "fetch"]); ap.add_argument("run"); ap.add_argument("arg", nargs="?")
    ap.add_argument("--creds", default="/tmp/drive_creds.json"); ap.add_argument("--hint", default="")
    a = ap.parse_args()
    tok = token(a.creds); parent = folder(tok)
    if a.cmd in ("request", "request-spec"):
        specs = build(a.arg) if a.cmd == "request" else json.load(open(a.arg))
        for k, v in specs.items():
            if ".." in k or k.startswith("/") or not v.get("lines"):
                sys.exit("bad spec key or empty lines: " + k)
            if v.get("tempos") and len(v["tempos"]) != len(v["lines"]):
                sys.exit("tempos must match lines: " + k)
            if v.get("names") and len(v["names"]) != len(v["lines"]):
                sys.exit("names must match lines: " + k)
        data = json.dumps({"run": a.run, "hint": a.hint, "specs": specs}).encode()
        meta = json.dumps({"name": f"req_{a.run}.json", "parents": [parent]}).encode()
        with req("POST", f"{API}/upload/drive/v3/files?uploadType=resumable", tok, meta,
                 {"Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": "application/json"}) as r:
            loc = r.headers["Location"]
        with req("PUT", loc, tok, data, {"Content-Type": "application/json"}) as r:
            json.load(r)
        print(json.dumps({"requested": a.run, "specs": {k: len(v["lines"]) for k, v in specs.items()},
                          "words": sum(len(" ".join(v["lines"]).split()) for v in specs.values())}))
        return
    done = find(tok, parent, f"done_{a.run}.json")
    if a.cmd == "status":
        if not done:
            print(json.dumps({"state": "pending" if find(tok, parent, f"req_{a.run}.json") else "missing"})); return
        d = json.loads(get(tok, done)); d["state"] = "ready" if d.get("ok") else "failed"; print(json.dumps(d)); return
    if not done or not json.loads(get(tok, done)).get("ok"):
        sys.exit("not ready (run `status`)")
    zid = find(tok, parent, f"vo_{a.run}.zip")
    z = zipfile.ZipFile(io.BytesIO(get(tok, zid)))
    root = os.path.abspath(a.arg)
    for n in z.namelist():
        p = os.path.abspath(os.path.join(root, n))
        if not p.startswith(root + os.sep):
            sys.exit("bad zip entry " + n)
    z.extractall(root)
    print(json.dumps({"fetched": a.run, "files": len(z.namelist()), "into": root}))

if __name__ == "__main__":
    main()
