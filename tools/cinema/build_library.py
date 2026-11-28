#!/usr/bin/env python3
"""Doc Cinema — build a small library of REAL recorded sounds + music beds from Openverse (no key needed).

Only licenses that allow use in monetized videos: CC0 and CC BY (attribution written to library.json / CREDITS.md).
Each sound: real onset found (leading silence cut), 5 ms fade-in, tail faded, peak-normalised, mp3 128k.
Run on the server: python3 build_library.py <out_dir>   (re-run safely; existing files are kept)
"""
import json, os, subprocess, sys, time, urllib.parse, urllib.request
import numpy as np, soundfile as sf

OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "library")
UA = {"User-Agent": "doc-cinema-library/1.0"}
# role → (queries, max seconds, how many to keep)
WANT = {
    "whoosh":      (["whoosh transition", "swoosh fast", "cinematic whoosh"], 3, 6),
    "riser":       (["cinematic riser", "tension riser", "suspense rise"], 8, 4),
    "impact":      (["cinematic impact boom", "deep hit trailer", "braam"], 6, 5),
    "hit_small":   (["soft hit percussion", "thud low", "tick hit"], 2, 4),
    "camera":      (["camera shutter", "polaroid shutter"], 2, 2),
    "paper":       (["paper document shuffle", "page turn"], 3, 3),
    "typewriter":  (["typewriter typing"], 6, 2),
    "radio":       (["radio static", "radio chatter static"], 8, 2),
    "glitch":      (["digital glitch", "data glitch"], 2, 3),
    "stamp":       (["rubber stamp", "stamp paper"], 2, 2),
    "amb_desert":  (["desert wind ambience", "wind dry ambience"], 60, 2),
    "amb_ocean":   (["ocean waves ambience", "sea ambience boat"], 60, 2),
    "amb_city":    (["city traffic ambience distant", "urban ambience night"], 60, 2),
    "amb_room":    (["room tone office", "room tone quiet"], 60, 2),
    "amb_industrial": (["construction site ambience", "factory machinery ambience"], 60, 2),
    "amb_engine":  (["airplane cabin ambience", "jet engine distant"], 60, 2),
    "helicopter":  (["helicopter flyover"], 20, 2),
    "siren":       (["police siren distant"], 15, 2),
}
MUSIC = {
    "music_tension": ["dark ambient tension", "suspense cinematic"],
    "music_documentary": ["documentary background", "cinematic documentary"],
    "music_drive": ["electronic pulse driving", "cinematic percussion"],
    "music_calm": ["calm ambient piano", "ambient pad"],
}
OK_LIC = {"cc0", "by"}


def api(params):
    url = "https://api.openverse.org/v1/audio/?" + urllib.parse.urlencode(params)
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.load(r).get("results", [])
        except Exception as e:
            print("  api retry", e, file=sys.stderr); time.sleep(3 + i * 3)
    return []


def fetch(url, path):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r, open(path, "wb") as f:
            f.write(r.read())
        return os.path.getsize(path) > 2000
    except Exception as e:
        print("  dl fail", e, file=sys.stderr); return False


def prep(src, dst, max_s, is_bed):
    tmp = dst + ".wav"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src, "-ac", "2", "-ar", "48000", tmp], check=True)
    a, sr = sf.read(tmp, dtype="float32")
    mono = np.abs(a).mean(axis=1)
    if mono.max() < 1e-3:
        os.remove(tmp); return None
    if not is_bed:  # real onset: first frame above 10% of peak (5 ms window)
        w = int(sr * 0.005); env = np.convolve(mono, np.ones(w) / w, mode="same")
        on = int(np.argmax(env > env.max() * 0.10)); a = a[max(0, on - int(sr * 0.003)):]
    a = a[: int(sr * max_s)]
    fi = int(sr * (0.005 if not is_bed else 1.0)); fo = int(sr * (0.15 if not is_bed else 2.0))
    a[:fi] *= np.linspace(0, 1, fi)[:, None]; a[-fo:] *= np.linspace(1, 0, fo)[:, None]
    a = a / max(1e-6, np.abs(a).max()) * (0.89 if not is_bed else 0.7)
    sf.write(tmp, a, sr)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", tmp, "-b:a", "128k" if not is_bed else "160k", dst], check=True)
    os.remove(tmp)
    return round(len(a) / sr, 2)


os.makedirs(OUT, exist_ok=True)
libf = os.path.join(OUT, "library.json")
lib = json.load(open(libf)) if os.path.exists(libf) else []
have = {e["id"] for e in lib}
jobs = [(role, qs, mx, n, False) for role, (qs, mx, n) in WANT.items()] + [(role, qs, 240, 3, True) for role, qs in MUSIC.items()]
for role, queries, max_s, keep, is_music in jobs:
    got = sum(1 for e in lib if e["role"] == role)
    for q in queries:
        if got >= keep:
            break
        params = {"q": q, "page_size": 20, "license": "cc0,by"}
        if is_music:
            params["category"] = "music"
        else:
            params["source"] = "freesound"
        for r in api(params):
            if got >= keep:
                break
            lic = (r.get("license") or "").lower()
            dur = (r.get("duration") or 0) / 1000
            if lic not in OK_LIC or r["id"] in have or not r.get("url"):
                continue
            if is_music and not (60 <= dur <= 600):
                continue
            if not is_music and dur and dur > max_s * 4:
                continue
            raw = os.path.join(OUT, "_raw_" + r["id"])
            if not fetch(r["url"], raw):
                continue
            fn = f"{role}_{got + 1:02d}.mp3"
            try:
                length = prep(raw, os.path.join(OUT, fn), max_s, is_music or role.startswith("amb_"))
            except Exception as e:
                print("  prep fail", e, file=sys.stderr); length = None
            os.remove(raw)
            if not length:
                continue
            lib.append({"id": r["id"], "role": role, "file": fn, "seconds": length, "title": r.get("title"), "creator": r.get("creator"),
                        "license": lic, "license_url": r.get("license_url"), "source": r.get("foreign_landing_url"), "query": q})
            have.add(r["id"]); got += 1
            print(role, fn, length, "s", lic, "|", (r.get("title") or "")[:50], flush=True)
            time.sleep(1.1)
        time.sleep(1.1)
json.dump(lib, open(libf, "w"), ensure_ascii=False, indent=1)
with open(os.path.join(OUT, "CREDITS.md"), "w") as f:
    f.write("# Sound & music credits (Doc Cinema library)\nAll CC0 or CC BY. For CC BY items put the line in the video description.\n\n")
    for e in lib:
        if e["license"] == "by":
            f.write(f"- \"{e['title']}\" by {e['creator']} — CC BY ({e['license_url']}) — {e['source']}\n")
print("library", len(lib), "items")
