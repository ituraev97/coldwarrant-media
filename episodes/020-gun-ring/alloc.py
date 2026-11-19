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
 BOTA=("FILE FOOTAGE · CBP, BRIDGE OF THE AMERICAS PORT OF ENTRY", "EL PASO, TEX., JULY 2024" + NC + "CBP VIA DVIDS"),
 BOTAMX=("FILE FOOTAGE · LANES INTO MEXICO, BRIDGE OF THE AMERICAS", "EL PASO, TEX., JULY 2024" + NC + "CBP VIA DVIDS"),
 BAIR=("FILE FOOTAGE · BRIDGE OF THE AMERICAS PORT OF ENTRY, AERIAL", "EL PASO, TEX., JULY 2024" + NC + "CBP VIA DVIDS"),
 NOG=("FILE FOOTAGE · CBP & NATIONAL GUARD VEHICLE INSPECTIONS", "NOGALES, ARIZ., AUG. 2018" + NC + "CBP VIA DVIDS"),
 LRD=("FILE FOOTAGE · BORDER PATROL & SOLDIERS NEAR LAREDO", "LAREDO, TEX., MARCH 2025" + NC + "U.S. ARMY VIA DVIDS"),
 SAV=("FILE FOOTAGE · CBP OFFICERS INSPECT OUTBOUND SHIPMENTS", "PORT OF SAVANNAH, GA., JUNE 2023" + NC + "CBP VIA DVIDS"),
 K9=("FILE FOOTAGE · CBP VEHICLE INSPECTION", "EL PASO, TEX., JULY 2024" + NC + "CBP VIA DVIDS"),
 STRAW=("ATF RETAILER TRAINING VIDEO \"DON'T LIE FOR THE OTHER GUY\"", "2014 · ACTORS, DRAMATIZATION" + NC + "ATF VIA DVIDS"),
 DISP=("FILE FOOTAGE · SEIZED WEAPONS SHOWN AT A CBP PRESS EVENT", "NOGALES, ARIZ., MAY 2025" + NC + "CBP VIA DVIDS"),
 LAR=("FILE FOOTAGE · CBP, HSI & ATF EVENT ON SOUTHBOUND WEAPONS", "LAREDO, TEX., JUNE 2025" + NC + "CBP VIA DVIDS"),
 PRESS=("FILE FOOTAGE · CBP PRESS CONFERENCE ON SOUTHBOUND WEAPONS", "NOGALES, ARIZ., MAY 2025" + NC + "CBP VIA DVIDS"),
 RIO=("FILE FOOTAGE · COAST GUARD PATROL ON THE RIO GRANDE", "RIO GRANDE CITY, TEX., OCT. 2026" + NC + "U.S. ARMY / JTF-SB VIA DVIDS"),
 LAB=("FILE FOOTAGE · ATF CRIME GUN INTELLIGENCE LAB", "WICHITA, KAN., 2026" + NC + "ATF VIA DVIDS"),
 HSIB=("FILE FOOTAGE · HSI TEAM BRIEFING BEFORE A WARRANT", "MISSION, TEX., APRIL 2024" + NC + "ICE / HSI VIA DVIDS"),
 HSI1=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM SERVES A WARRANT", "MISSION, TEX., APRIL 2024" + NC + "ICE / HSI VIA DVIDS"),
 HSI2=("FILE FOOTAGE · HSI SPECIAL AGENTS SERVE WARRANTS", "AUG. 2024" + NC + "DHS VIA DVIDS"),
)
CL = {
 "BOTA": ("936098", [(10.5, 48), (50, 88)], "BOTA", {}),
 "BOTAMX": ("936098", [(135, 178)], "BOTAMX", {}),
 "BAIR": ("936097", [(16, 246)], "BAIR", {}),
 "NOG": ("617217", [(16, 135)], "NOG", {}),
 "LRD": ("957002", [(8, 50)], "LRD", {}),
 "SAV": ("891569", [(8, 95), (96, 280), (288, 360)], "SAV", {}),
 "K9": ("936098", [(88, 116)], "K9", {}),
 "STRAW": ("350830", [(0.5, 12), (30, 44), (180, 206), (420, 530)], "STRAW", {}),
 "DISP": ("960896", [(12, 23), (26, 35), (36, 50), (60, 87)], "DISP", {}),
 "LAR": ("965069", [(300, 309), (650, 674)], "LAR", {}),
 "PRESS": ("960915", [(30, 110), (960, 1830)], "PRESS", {}),
 "RIO": ("1026422", [(0.5, 115)], "RIO", {}),
 "LAB": ("1007053", [(10, 14), (25, 29), (45, 54), (65, 74), (80, 84), (100, 104), (120, 124), (130, 134), (140, 150)], "LAB", {}),
 "HSIB": ("950625", [(15, 58)], "HSIB", {}),
 "HSI1": ("950625", [(60, 118), (155, 200), (240, 262)], "HSI1", {}),
 "HSI2": ("935309", [(110, 160)], "HSI2", {}),
}
POOL = {"PORT": ["BAIR", "BOTA", "NOG", "LRD"], "BRIDGE": ["BOTAMX", "BAIR", "NOG", "BOTA"], "OUT": ["SAV", "NOG", "K9", "BOTAMX"],
        "STRAW": ["STRAW"], "DISPLAY": ["DISP", "LAR", "PRESS", "BAIR"], "RIVER": ["RIO", "LRD"], "SQUAD": ["HSIB", "LAB", "SAV", "PRESS"],
        "RAID": ["HSI1", "HSI2"], "LAREDO": ["LAR", "PRESS"]}
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
order_idx = sorted(range(len(E.LINES)), key=lambda i: 0)
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
