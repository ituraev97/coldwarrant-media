#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py (027; from 024/alloc.py).
Before TTS (no vo/raw_NN.wav) spoken durations are ESTIMATED from word count (2.9 words/s at the 1.15 scale); re-run after TTS."""
import json, os, re, math, subprocess, importlib.util, sys
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
sys.path.insert(0, EP)
from respell import respell
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
NC = " · NOT BOLIVIA · NOT THIS CASE"
T = dict(
 AIRT=("FILE FOOTAGE · U.S. CBP P-3 SURVEILLANCE AIRCRAFT, GULF OF MEXICO", "2015" + NC + " · CBP VIA DVIDS"),
 BIGT=("FILE FOOTAGE · JIATF SOUTH AIR AND MARITIME DETECTION", "2025" + NC + " · U.S. SOUTHERN COMMAND VIA DVIDS"),
 BOATAT=("FILE FOOTAGE · AERIAL VIEW OF A SMUGGLING BOAT, EASTERN PACIFIC", "JAN. 2025" + NC + " · U.S. COAST GUARD VIA DVIDS"),
 BOATBT=("FILE FOOTAGE · AIRCRAFT TRACKS A SUSPECT BOAT OFF ECUADOR", "JAN. 2025" + NC + " · U.S. COAST GUARD VIA DVIDS"),
)
CL = {
 "AIR": ("403639", [(5.0, 195.0), (200.0, 400.0)], "AIRT", {}),
 "BIG": ("968690", [(240.0, 250.0), (264.0, 276.0), (300.0, 330.0)], "BIGT", {}),
 "BOATA": ("958198", [(1.0, 76.0)], "BOATAT", {}),
 "BOATB": ("958200", [(1.0, 125.0)], "BOATBT", {}),
}
POOL = {"AIR": ["AIR"], "BIG": ["BIG", "AIR"], "BOAT": ["BOATA", "BOATB"], "MP": ["AIR", "BOATA", "BOATB"]}
OWN = set()
blocked = {}
for u in json.load(open(f"{ROOT}/used_clips.json")):
    if str(u["clip"]) in OWN: continue
    blocked.setdefault(str(u["clip"]), []).append((u["start"] - 0.2, u["start"] + 7.0))
for line in open("/home/claude/work/c027_black.txt").read().splitlines():
    if not line[:1].isdigit(): continue
    cid = line.split()[0]
    for a, b in re.findall(r"black_start:([0-9.]+) black_end:([0-9.]+)", line):
        blocked.setdefault(cid, []).append((float(a) - 0.3, float(b) + 0.3))
taken = {}
def free(cid, a, b, strict=True):
    bl = blocked.get(cid, []) + (taken.get(cid, []) if strict else [])
    return all(not (a < y and x < b) for x, y in bl)
cursor = {}
def take(key, d):
    cid, ranges, tk, so = CL[key]
    cands = []
    for ra, rb in ranges:
        t = ra
        while t + d <= rb - 0.1: cands.append(round(t, 1)); t += 0.5
    c0 = cursor.get(key, 0)
    order = [x for x in cands if x >= c0] + [x for x in cands if x < c0]
    for s in order:
        if free(cid, s, s + d):
            taken.setdefault(cid, []).append((s, s + d)); cursor[key] = s + d; return s
    if cid in OWN:  # short case clips: allow reuse (least-overlapped start), never black
        best = None
        for s in order:
            if not free(cid, s, s + d, strict=False): continue
            ov = sum(max(0, min(y, s + d) - max(x, s)) for x, y in taken.get(cid, []))
            if best is None or ov < best[0]: best = (ov, s)
        if best:
            taken.setdefault(cid, []).append((best[1], best[1] + d)); cursor[key] = best[1] + d; return best[1]
    return None
def _vd(i):
    f = f"{EP}/vo/raw_{i:02d}.wav"
    return dur(f) if os.path.exists(f) else len(E.LINES[i - 1][0].split()) / 2.9
vd = [_vd(i) for i in range(1, len(E.LINES) + 1)]
out, problems, rot = {}, [], {}
EXTRA = {10: 2, 25: 2, 27: 2, 33: 3, 39: 3, 44: 3, 58: 2}
for i in range(len(E.LINES)):
    txt, shots, o = E.LINES[i]
    # post-TTS: keep every footage shot <= 6.2 s (build_ep divides a line equally among its shots)
    if (i + 1) in EXTRA: shots = list(shots) + [("pool:MP", 0, {})] * EXTRA[i + 1]
    if (i + 1) == 23: shots = list(shots) + [("img:face", 0, {"kb": "pan"}), ("img:still", 0, {"kb": "in"})]
    if all(s_[0].startswith("g:") for s_ in shots) and vd[i] + o.get("gap", 0.45) > 10 and not shots[0][0].startswith(("g:chapter", "g:title", "g:end")):
        shots = list(shots) + [("pool:MP", 0, {})]
    pools = [s[0][5:] for s in shots if s[0].startswith("pool:")]
    if not pools: out[i] = (respell(txt), shots, o); continue
    L = vd[i] + o.get("gap", 0.45) + (1.0 if i == 0 else 0)
    fixed = [s_ for s_ in shots if not s_[0].startswith("pool:")]
    npool = len(pools) if fixed else max(len(pools), math.ceil(L / 6.2))
    d = L / (npool + len(fixed)) + 0.25
    order = POOL[pools[0]]; r = rot.get(pools[0], 0); order = order[r:] + order[:r]; rot[pools[0]] = (r + 1) % len(POOL[pools[0]])
    got = None
    for key in order + [k for k in POOL["MP"] if k not in order]:
        starts = []
        for _ in range(npool):
            s = take(key, d)
            if s is None: break
            starts.append(s)
        if len(starts) == npool: got = key; break
        cid = CL[key][0]
        for s in starts: taken[cid].remove((s, s + d))
    if got:
        cid, _, tk, so = CL[got]
        it = iter(starts)
        base = {} if so.get("lab") == 0 else {"lab": 1}
        newsh = [s_ if not s_[0].startswith("pool:") else (cid, next(it), dict(base, **so)) for s_ in shots]
        newsh += [(cid, x, dict(base, **so)) for x in it]
        o3 = dict(o) if (fixed or "tag" in o) else dict(o, tag=T[tk], lab=so.get("lab", 1))
        out[i] = (respell(txt), newsh, o3)
    else:
        problems.append((i + 1, pools, round(d, 1))); out[i] = (respell(txt), shots, o)
out = [out[i] for i in range(len(E.LINES))]
print("problems:", problems)
src = open(f"{EP}/episode_src.py").read()
head = src[:src.index("LINES = [")]; tail = src[src.index("\ndef _L("):]
body = "LINES = [\n" + "".join(f" ({t!r},\n  {sh!r},\n  {o!r}),\n" for t, sh, o in out) + "]\n"
open(f"{EP}/episode.py", "w").write(head.replace("pool placeholders", "pool placeholders (RESOLVED by alloc.py)") + body + tail)
json.dump(taken, open(f"{EP}/alloc_taken.json", "w"))
print("shots > 6.5 s:", [(i + 1, round((vd[i] + o.get("gap", 0.45)) / len(sh), 1)) for i, (t, sh, o) in enumerate(out) if (vd[i] + o.get("gap", 0.45)) / len(sh) > 6.5])
print("total s", round(sum(vd) + sum(o.get("gap", 0.45) for _, _, o in E.LINES) + 1, 1))
