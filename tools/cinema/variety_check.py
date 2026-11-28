#!/usr/bin/env python3
"""Variety check on a FINISHED video (owner 2026-11-28: "the same clips and graphics keep coming back").
Works for any channel's pipeline: looks only at the picture. 1 frame/s -> 64-bit perceptual hash.
  repeat_share  = share of seconds whose picture already appeared >= 8 s earlier (re-shown clip moment / still / doc page)
  top_visual    = share of seconds taken by the single most-shown picture (one clip/still/card dominating)
  cross_share   = share of seconds that match pictures of the channel's previous episodes (ledger)
Usage: python3 variety_check.py VIDEO [--ledger variety_ledger.json --episode ID] [--max-repeat 0.15 --max-top 0.12 --max-cross 0.10]
Writes VIDEO.variety.json, prints one JSON line, exit 1 = FAIL. Needs ffmpeg + numpy only.
After a PASS (or an owner-accepted run) it appends this episode's hashes to the ledger (keeps the last 8 episodes).
"""
import argparse, json, os, subprocess, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("--ledger"); ap.add_argument("--episode")
ap.add_argument("--max-repeat", type=float, default=0.15); ap.add_argument("--max-top", type=float, default=0.12)
ap.add_argument("--max-cross", type=float, default=0.10); ap.add_argument("--fps", type=float, default=1.0)
a = ap.parse_args()

W, H = 17, 16
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", a.video, "-vf", f"fps={a.fps},scale={W*4}:{H*4},format=gray", "-f", "rawvideo", "-"],
                     capture_output=True, check=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H * 4, W * 4).astype(np.float32)
small = fr.reshape(-1, H, 4, W, 4).mean(axis=(2, 4))               # 8x9 block means
bits = (small[:, :, 1:] > small[:, :, :-1]).reshape(len(fr), -1)    # dHash 256 bits
contrast = fr.std(axis=(1, 2))
valid = contrast > 12                                               # skip black / flat frames (fades, blanks)
hashes = np.packbits(bits, axis=1)

def ham(x, ys):
    return np.unpackbits(np.bitwise_xor(ys, x), axis=1).sum(1)

N = len(hashes); TH = int(__import__('os').environ.get('VC_TH', 22)); GAP = int(8 * a.fps)
# shots: a new shot starts where the picture changes; a slow push/pan inside one shot is NOT a repeat
shot = np.zeros(N, int)
for i in range(1, N):
    shot[i] = shot[i - 1] + (1 if ham(hashes[i], hashes[i - 1:i])[0] > TH else 0)
rep = np.zeros(N, bool)
for i in range(N):
    if valid[i] and i > GAP:
        k = np.where(valid[:i - GAP] & (shot[:i - GAP] < shot[i] - 1))[0]   # earlier, different shots only
        if len(k) and ham(hashes[i], hashes[k]).min() <= TH:
            rep[i] = True
if os.environ.get("VC_PAIRS"):
    pr = [(int(i), int(np.argmin(ham(hashes[i], hashes[:i - GAP])))) for i in np.where(rep)[0][:: max(1, rep.sum() // 6)][:6]]
    print("PAIRS", pr)
# most-shown picture: count of near-duplicates per valid frame
vi = np.where(valid)[0]; best = 0
for i in vi[:: max(1, len(vi) // 400)]:
    best = max(best, int((ham(hashes[i], hashes[vi]) <= TH).sum()))
nv = max(1, len(vi))
res = {"video": os.path.basename(a.video), "seconds": round(N / a.fps), "checked": int(nv),
       "repeat_share": round(float(rep[valid].mean()) if nv else 0, 3), "top_visual": round(best / nv, 3)}
cross = None
if a.ledger:
    L = json.load(open(a.ledger)) if os.path.exists(a.ledger) else {"episodes": []}
    old = [bytes.fromhex(h) for e in L["episodes"] if e["id"] != a.episode for h in e["h"]]
    if old:
        O = np.frombuffer(b"".join(old), np.uint8).reshape(-1, hashes.shape[1])
        m = np.array([ham(hashes[i], O).min() <= TH for i in vi])
        cross = round(float(m.mean()), 3)
    res["cross_share"] = cross
fails = []
if res["repeat_share"] > a.max_repeat: fails.append(f"repeat_share {res['repeat_share']} > {a.max_repeat}: the same clip moments/stills/pages are shown again")
if res["top_visual"] > a.max_top: fails.append(f"top_visual {res['top_visual']} > {a.max_top}: one picture dominates")
if cross is not None and cross > a.max_cross: fails.append(f"cross_share {cross} > {a.max_cross}: pictures reused from previous episodes")
res["verdict"] = "FAIL" if fails else "PASS"; res["fails"] = fails
json.dump(res, open(a.video + ".variety.json", "w"), indent=1)
if a.ledger and a.episode:
    L = json.load(open(a.ledger)) if os.path.exists(a.ledger) else {"episodes": []}
    L["episodes"] = [e for e in L["episodes"] if e["id"] != a.episode][-7:] + [{"id": a.episode, "h": [hashes[i].tobytes().hex() for i in vi]}]
    json.dump(L, open(a.ledger, "w"))
print(json.dumps(res))
sys.exit(1 if fails else 0)
