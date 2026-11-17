#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py (pattern from 017/alloc.py).
One clip family per line so the FILE FOOTAGE tag matches the picture; <= 6.2 s per shot; avoids used_clips.json,
blackdetect windows (/home/claude/work/black.txt) and overlaps."""
import json, os, re, math, subprocess, importlib.util
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
NC = " · NOT THIS CASE · "
T = dict(
 GN=("FILE FOOTAGE · GUATEMALAN SAILORS & U.S. NAVY DRUG-INTERDICTION EXERCISE", "PORT SAN JOSÉ, GUATEMALA, MAY 2025" + NC + "U.S. AIR FORCE VIA DVIDS"),
 CG=("FILE FOOTAGE · COAST GUARD CHASES SMUGGLING BOATS OFF GUATEMALA", "JULY 8, 2009 · INFRARED" + NC + "U.S. COAST GUARD VIA DVIDS"),
 SS=("FILE FOOTAGE · COAST GUARD BOARDS A SEMI-SUBMERSIBLE, EASTERN PACIFIC", "NOV. 2023" + NC + "U.S. COAST GUARD VIA DVIDS"),
 SF=("FILE FOOTAGE · COAST GUARD BOAT APPROACHES A SEMI-SUBMERSIBLE", "FEB. 2026" + NC + "U.S. COAST GUARD VIA DVIDS"),
 OF1=("FILE FOOTAGE · COAST GUARD COCAINE OFFLOAD, FLORIDA", "JUNE 2026" + NC + "U.S. COAST GUARD VIA DVIDS"),
 OF2=("FILE FOOTAGE · COAST GUARD COCAINE OFFLOAD, MIAMI BEACH", "APRIL 2026" + NC + "U.S. COAST GUARD VIA DVIDS"),
 OF3=("FILE FOOTAGE · COAST GUARD COCAINE OFFLOAD, FLORIDA", "JULY 2025" + NC + "U.S. COAST GUARD VIA DVIDS"),
 OF4=("FILE FOOTAGE · COAST GUARD COCAINE OFFLOAD, FLORIDA", "APRIL 2025" + NC + "U.S. COAST GUARD VIA DVIDS"),
 OF5=("FILE FOOTAGE · COAST GUARD COCAINE OFFLOAD, FLORIDA", "MAY 2025" + NC + "U.S. COAST GUARD VIA DVIDS"),
 HM=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM, TEXAS", "APRIL 2024" + NC + "ICE / HSI VIA DVIDS"),
 HN=("FILE FOOTAGE · HSI SPECIAL AGENTS SERVE WARRANTS, TEXAS", "AUG. 2024" + NC + "ICE / HSI VIA DVIDS"),
 EX=("FILE FOOTAGE · AN EXTRADITION FLIGHT ARRIVES, OMAHA", "2025" + NC + "ICE VIA DVIDS"),
 K9=("FILE FOOTAGE · U.S. ARMY GREEN BERETS TRAIN GUATEMALAN K-9 HANDLERS", "GUATEMALA, MARCH 2023" + NC + "U.S. ARMY VIA DVIDS"),
 TC=("FILE FOOTAGE · HSI / FBI TRANSFER OF CUSTODY, MIAMI", "SEPT. 2026" + NC + "ICE / HSI VIA DVIDS"),
)
CL = {  # key: (clip, allowed ranges, tag key, shot opts)
 "GN": ("962843", [(1, 75.8)], "GN", {}),
 "CG": ("314347", [(12, 94.5), (107, 147)], "CG", {"pb": 1}),
 "SS": ("911825", [(1, 144)], "SS", {}),
 "SF": ("999256", [(0.5, 14.3)], "SF", {}),
 "OF1": ("1012550", [(1, 44.5)], "OF1", {}),
 "OF2": ("1002828", [(1, 35.5)], "OF2", {}),
 "OF3": ("972021", [(1, 77.5)], "OF3", {}),
 "OF4": ("958225", [(1, 72)], "OF4", {}),
 "OF5": ("962790", [(6, 51)], "OF5", {}),
 "HM": ("950625", [(10, 271)], "HM", {}),
 "HN": ("935309", [(5, 162)], "HN", {}),
 "EX": ("956175", [(6, 42.5)], "EX", {}),
 "TC": ("1024394", [(10, 150)], "TC", {}),
 "K9": ("877563", [(100, 174), (296, 333), (1, 74)], "K9", {"pb": 1}),
}
POOL = {"BERT": ["CG"], "GUAT": ["GN", "K9"], "CGG": ["CG", "SS"], "SEMI": ["SS", "SF", "CG"], "OFFLOAD": ["OF4", "OF3", "OF1", "OF5", "OF2"],
        "HSI": ["HM", "HN"], "EXTRA": ["TC", "EX", "HN"]}
blocked = {}
for u in json.load(open(f"{ROOT}/used_clips.json")):
    blocked.setdefault(str(u["clip"]), []).append((u["start"] - 0.2, u["start"] + 7.0))
for line in open("/home/claude/work/black.txt").read().splitlines():
    if not line[:1].isdigit(): continue
    cid = line.split()[0]
    for a, b in re.findall(r"black_start:([0-9.]+) black_end:([0-9.]+)", line):
        blocked.setdefault(cid, []).append((float(a) - 0.3, float(b) + 0.3))
taken = {}
def free(cid, a, b): return all(not (a < y and x < b) for x, y in blocked.get(cid, []) + taken.get(cid, []))
cursor = {}
def take(key, d):
    cid, ranges, tk, so = CL[key]
    cands = []
    for ra, rb in ranges:
        t = ra
        while t + d <= rb - 0.1: cands.append(round(t, 1)); t += 0.5
    c0 = cursor.get(key, 0)
    for s in [x for x in cands if x >= c0] + [x for x in cands if x < c0]:
        if free(cid, s, s + d):
            taken.setdefault(cid, []).append((s, s + d)); cursor[key] = s + d; return s
    return None
vd = [dur(f"{EP}/vo/raw_{i:02d}.wav") for i in range(1, len(E.LINES) + 1)]
out, problems, rot = {}, [], {}
order_idx = sorted(range(len(E.LINES)), key=lambda i: 0 if "pool:BERT" in str(E.LINES[i][1]) else 1)
for i in order_idx:
    txt, shots, o = E.LINES[i]
    pools = [s[0][5:] for s in shots if s[0].startswith("pool:")]
    if not pools: out[i] = (txt, shots, o); continue
    L = vd[i] + o.get("gap", 0.45) + (1.0 if i == 0 else 0)
    fixed = [s_ for s_ in shots if not s_[0].startswith("pool:")]
    npool = len(pools) if fixed else max(len(pools), math.ceil(L / 6.2))
    d = L / (npool + len(fixed)) + 0.25
    order = POOL[pools[0]]; r = rot.get(pools[0], 0); order = order[r:] + order[:r]; rot[pools[0]] = (r + 1) % len(POOL[pools[0]])
    got = None
    for key in order:
        starts = []
        for _ in range(npool):
            s = take(key, d)
            if s is None: break
            starts.append(s)
        if len(starts) == npool: got = key; break
        cid = CL[key][0]
        for s in starts: taken[cid].remove((s, s + d))
    o2 = dict(o)
    if got:
        cid, _, tk, so = CL[got]
        it = iter(starts); newsh = [s_ if not s_[0].startswith("pool:") else (cid, next(it), dict(so, lab=1)) for s_ in shots]
        newsh += [(cid, x, dict(so, lab=1)) for x in it]
        o3 = dict(o2) if fixed else dict(o2, tag=T[tk], lab=1)
        pass
        out[i] = (txt, newsh, o3)
    else:
        problems.append((i + 1, pools, round(d, 1))); out[i] = (txt, shots, o2)
out = [out[i] for i in range(len(E.LINES))]
print("problems:", problems)
src = open(f"{EP}/episode_src.py").read()
head = src[:src.index("LINES = [")]; tail = src[src.index("\ndef _L("):]
body = "LINES = [\n" + "".join(f" ({t!r},\n  {sh!r},\n  {o!r}),\n" for t, sh, o in out) + "]\n"
open(f"{EP}/episode.py", "w").write(head.replace("pool placeholders", "pool placeholders (RESOLVED by alloc.py)") + body + tail)
json.dump(taken, open(f"{EP}/alloc_taken.json", "w"))
print("shots > 6.5 s:", [(i + 1, round((vd[i] + o.get("gap", 0.45)) / len(sh), 1)) for i, (t, sh, o) in enumerate(out) if (vd[i] + o.get("gap", 0.45)) / len(sh) > 6.5])
print("total s", round(sum(vd) + sum(o.get("gap", 0.45) for _, _, o in E.LINES) + 1, 1))
