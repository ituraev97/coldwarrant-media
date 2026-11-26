#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py (024; from 023/alloc.py).
Case-own clips (695886 boarding, 696129 offload, 712936 Pence) are short: reuse allowed, used_clips block ignored for them."""
import json, os, re, math, subprocess, importlib.util, sys
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
sys.path.insert(0, EP)
from respell import respell
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
CG = "U.S. COAST GUARD VIA DVIDS"
NC = " · NOT THE SEXTON CASES · "
T = dict(
 SEXT=("OCT. 28, 2026 · ~175 MI OFF CARTAGENA · TWO SUSPECTED DRUG BOATS", "U.S. COAST GUARD VIDEO VIA DVIDS"),
 OFFLNT=("CUTTER LAWRENCE LAWSON OFFLOAD · BASE MIAMI BEACH · NOV. 17, 2026", "U.S. COAST GUARD VIDEO VIA DVIDS · NOV. 4 SEXTON CASE"),
 FRCT=("FILE FOOTAGE · FAST RESPONSE CUTTER BERNARD WEBBER OFFLOAD", "BASE MIAMI BEACH, OCT. 2018" + NC + CG),
 GOFT=("FILE FOOTAGE · COAST GUARD INTERDICTS A GO-FAST VESSEL", "2021–2025" + NC + CG),
 OFFT=("FILE FOOTAGE · COAST GUARD OFFLOAD", "2020–2026" + NC + CG),
)
CL = {
 "SEXA": ("1029779", [(0.5, 68.0)], "SEXT", {"lab": 0}),
 "SEXB": ("1029779", [(70.0, 122.5)], "SEXT", {"lab": 0}),
 "OFFLN": ("1030153", [(0.5, 34.5)], "OFFLNT", {"lab": 0}),
 "FRC1": ("633088", [(1.0, 71.0)], "FRCT", {}),
 "G1": ("974643", [(1.0, 69.5)], "GOFT", {}),
 "G2": ("786446", [(1.0, 22.5)], "GOFT", {}),
 "G3": ("831656", [(1.0, 28.5)], "GOFT", {"pb": 1}),
 "O1": ("765240", [(1.0, 32.0)], "OFFT", {}),
 "O2": ("1003784", [(1.0, 36.0)], "OFFT", {}),
 "O3": ("1000233", [(1.0, 62.0)], "OFFT", {"vert": 1}),
 "O4": ("991450", [(1.0, 36.0)], "OFFT", {"vert": 1}),
 "G4": ("989481", [(1.0, 27.5)], "GOFT", {}),
 "G5": ("978313", [(1.0, 18.5)], "GOFT", {}),
 "G6": ("960770", [(1.0, 26.0)], "GOFT", {}),
 "O5": ("954535", [(1.0, 58.0)], "OFFT", {}),
 "O6": ("931356", [(1.0, 50.0)], "OFFT", {}),
 "O7": ("906544", [(1.0, 70.0)], "OFFT", {}),
}
POOL = {"SEXA": ["SEXA", "SEXB"], "SEXB": ["SEXB", "SEXA"], "OFFLN": ["OFFLN"], "FRC": ["FRC1"], "GOFAST": ["G1", "G4", "G2", "G6", "G3", "G5"],
        "OFFL": ["O1", "O2", "O5", "O6", "O7", "O3", "O4"], "MP": ["G1", "G4", "O5", "O1", "O6", "O2", "G6", "O7", "G2", "G3", "G5", "O3", "O4"]}
OWN = {"1029779", "1030153"}
blocked = {}
blocked["1000233"] = [(62.0, 70.0)]
for u in json.load(open(f"{ROOT}/used_clips.json")):
    if str(u["clip"]) in OWN: continue
    blocked.setdefault(str(u["clip"]), []).append((u["start"] - 0.2, u["start"] + 7.0))
for line in open("/home/claude/work/c026/black.txt").read().splitlines():
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
import os
def _vd(i):
    f = f"{EP}/vo/raw_{i:02d}.wav"
    if os.path.exists(f): return dur(f)
    n = len(E.LINES[i - 1][0].split()); return n / 3.0   # ESTIMATE (~180 wpm) until TTS exists: re-run after TTS
vd = [_vd(i) for i in range(1, len(E.LINES) + 1)]
print("durations:", "real" if os.path.exists(f"{EP}/vo/raw_01.wav") else "ESTIMATED")
out, problems, rot = {}, [], {}
for i in range(len(E.LINES)):
    txt, shots, o = E.LINES[i]
    if all(s_[0].startswith("g:") for s_ in shots) and vd[i] + o.get("gap", 0.45) > 7.5 and not shots[0][0].startswith(("g:chapter", "g:title", "g:end")):
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
