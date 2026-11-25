#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py (024; from 023/alloc.py).
Case-own clips (695886 boarding, 696129 offload, 712936 Pence) are short: reuse allowed, used_clips block ignored for them."""
import json, os, re, math, subprocess, importlib.util, sys
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
sys.path.insert(0, EP)
from respell import respell
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
NC = " · NOT THE MUNRO BOARDING · "
CG = "U.S. COAST GUARD VIA DVIDS"
T = dict(
 BOARDT=("MUNRO BOARDING TEAM · EASTERN PACIFIC · JUNE 18, 2019", "COAST GUARD VIDEO VIA DVIDS"),
 OFFL19T=("MUNRO OFFLOAD · NAS NORTH ISLAND, SAN DIEGO · JULY 11, 2019", "U.S. COAST GUARD VIA DVIDS"),
 PENCET=("VICE PRESIDENT MIKE PENCE · MUNRO OFFLOAD · JULY 11, 2019", "U.S. COAST GUARD VIA DVIDS"),
 SUB16T=("FILE FOOTAGE · COAST GUARD BOARDS A SEMI-SUBMERSIBLE", "EASTERN PACIFIC, 2016" + NC + CG),
 UNDERT=("FILE FOOTAGE · UNDERWATER VIEW OF A SEMI-SUBMERSIBLE HULL", "2016" + NC + CG),
 SUB15T=("FILE FOOTAGE · CUTTER STRATTON + A SEMI-SUBMERSIBLE", "EASTERN PACIFIC, JULY 2015" + NC + CG),
 SUB16BT=("FILE FOOTAGE · COAST GUARD CREW INSPECTS A SEMI-SUBMERSIBLE", "EASTERN PACIFIC, 2016" + NC + CG),
 OFFL16T=("FILE FOOTAGE · COAST GUARD OFFLOADS ABOUT 14 TONS OF COCAINE", "SAN DIEGO, APRIL 2016 · NOT THE MUNRO OFFLOAD · " + CG),
 GOFT=("FILE FOOTAGE · COAST GUARD INTERDICTS A SMUGGLING BOAT", "EASTERN PACIFIC, 2018–2019 · NOT THE MUNRO PATROL · " + CG),
 MUN24T=("FILE FOOTAGE · CUTTER MUNRO CREW, EASTERN PACIFIC", "OCT. 2024 · NOT THE 2019 PATROL · " + CG),
 MUN24BT=("FILE FOOTAGE · CUTTER MUNRO OFFLOADS COCAINE", "SAN DIEGO, MAY 2024 · NOT THE 2019 OFFLOAD · " + CG),
 MUN25T=("FILE FOOTAGE · CUTTER MUNRO, EASTERN PACIFIC", "DEC. 2025 · NOT THE 2019 PATROL · " + CG),
 HELIT=("FILE FOOTAGE · COAST GUARD HELICOPTER CREW (HITRON) AT SEA", "EASTERN PACIFIC, DEC. 2025 · NOT THE 2019 PATROL · " + CG),
)
CL = {
 "BOARD": ("695886", [(1.0, 58.0)], "BOARDT", {"lab": 0}),
 "OFFL19": ("696129", [(1.0, 128.0)], "OFFL19T", {"lab": 0}),
 "OFFL19B": ("712936", [(9.0, 26.5)], "OFFL19T", {"lab": 0}),
 "PENCE": ("712936", [(3.5, 8.6), (27.0, 29.8), (51.0, 62.5)], "PENCET", {"lab": 0}),
 "SUB16": ("456013", [(15.0, 95.0)], "SUB16T", {}),
 "UNDER": ("456013", [(100.0, 160.0)], "UNDERT", {}),
 "SUB15": ("418232", [(48.0, 76.0), (80.0, 205.0)], "SUB15T", {}),
 "SUB16B": ("489533", [(4.0, 98.0)], "SUB16BT", {}),
 "OFFL16": ("457944", [(5.0, 38.0), (46.0, 134.0)], "OFFL16T", {}),
 "G1": ("699077", [(1.0, 70.0), (79.0, 88.0)], "GOFT", {}), "G2": ("733776", [(1.0, 15.0)], "GOFT", {}), "G3": ("590286", [(86.0, 118.0)], "GOFT", {}),
 "MUN24": ("944124", [(15.0, 29.0)], "MUN24T", {}), "MUN24B": ("925292", [(2.0, 58.0)], "MUN24BT", {}),
 "MUN25a": ("989074", [(4.0, 78.0)], "MUN25T", {}), "MUN25b": ("989076", [(2.0, 96.0)], "MUN25T", {}),
 "HELI": ("989073", [(2.0, 67.0)], "HELIT", {}),
}
POOL = {"BOARD": ["BOARD"], "OFFL19": ["OFFL19", "OFFL19B"], "PENCE": ["PENCE"], "SUB16": ["SUB16", "SUB16B"], "UNDER": ["UNDER"], "SUB15": ["SUB15", "SUB16B"],
        "SUB16B": ["SUB16B", "SUB16"], "OFFL16": ["OFFL16"], "GOFAST": ["G1", "G3", "G2"], "MUN24": ["MUN24", "MUN24B"], "MUN25": ["MUN25a", "MUN25b"], "HELI": ["HELI", "MUN25b"],
        "MP": ["SUB16", "SUB15", "OFFL16", "MUN25a"]}
OWN = {"695886", "696129", "712936"}
blocked = {}
for u in json.load(open(f"{ROOT}/used_clips.json")):
    if str(u["clip"]) in OWN: continue
    blocked.setdefault(str(u["clip"]), []).append((u["start"] - 0.2, u["start"] + 7.0))
for line in open("/home/claude/work/black.txt").read().splitlines():
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
vd = [dur(f"{EP}/vo/raw_{i:02d}.wav") for i in range(1, len(E.LINES) + 1)]
out, problems, rot = {}, [], {}
for i in range(len(E.LINES)):
    txt, shots, o = E.LINES[i]
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
