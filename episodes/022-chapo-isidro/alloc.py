#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py (022, from 021/alloc.py).
One clip family per line so the FILE FOOTAGE tag matches the picture; <= 6.2 s per shot; avoids used_clips.json,
blackdetect windows (/home/claude/work/black.txt) and overlaps."""
import json, os, re, math, subprocess, importlib.util
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
NC = " · NOT THIS OPERATION · "
T = dict(
 NI=("FILE FOOTAGE · MEXICAN NAVAL INFANTRY + U.S. MARINES, URBAN TRAINING", "RIMPAC 2026, HAWAII" + NC + "U.S. NAVY VIA DVIDS"),
 JNG=("FILE FOOTAGE · U.S. MARINES + MEXICAN NAVAL INFANTRY, FIELD TRAINING", "RIMPAC 2026, HAWAII" + NC + "U.S. NAVY VIA DVIDS"),
 HELI=("FILE FOOTAGE · MEXICAN FEDERAL POLICE HELICOPTERS IN ARIZONA", "OPERATION DIABLO EXPRESS, JAN. 2016" + NC + "ICE / HSI VIA DVIDS"),
 CONV=("FILE FOOTAGE · MEXICAN POLICE CROSS SOUTH AT LUKEVILLE, ARIZ.", "OPERATION DIABLO EXPRESS, JAN. 2016" + NC + "ICE / HSI VIA DVIDS"),
 FUER=("FILE FOOTAGE · MEXICAN, U.S. AND CANADIAN SOLDIERS, JOINT EXERCISE", "FUERZAS AMIGAS 2025, FORT HOOD, TEX." + NC + "U.S. ARMY VIA DVIDS"),
 FLAG=("FILE FOOTAGE · MEXICAN ARMY (SEDENA) SOLDIER IN TRAINING", "INDIAN HEAD, MD., 2021" + NC + "U.S. MARINE CORPS VIA DVIDS"),
 PAT=("FILE FOOTAGE · MEXICAN MILITARY + U.S. BORDER PATROL, MIRRORED PATROL", "TECATE, CALIF., SEPT. 2026" + NC + "CBP VIA DVIDS"),
 SEA=("FILE FOOTAGE · FBI TEN MOST WANTED ANNOUNCEMENT", "FBI SEATTLE, MARCH 2026" + NC + "FBI VIA DVIDS"),
 HQ=("FILE FOOTAGE · FBI HEADQUARTERS, J. EDGAR HOOVER BUILDING", "WASHINGTON, D.C., 2025 · FBI VIA DVIDS"),
 HSIR=("FILE FOOTAGE · HSI ENFORCEMENT OPERATION (FACES BLURRED BY HSI)", "OMAHA, NEB., AUG. 2026" + NC + "ICE / HSI VIA DVIDS"),
 RAID=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM, SEARCH WARRANT", "CHICAGO, OCT. 2022" + NC + "ICE / HSI VIA DVIDS"),
 FENT=("FILE FOOTAGE · CBP FENTANYL SEIZURE AT A PORT OF ENTRY", "SAN YSIDRO, CALIF., 2023" + NC + "CBP VIA DVIDS"),
 METH=("FILE FOOTAGE · SEIZED METH, HEROIN AND FENTANYL", "NOGALES, ARIZ., 2023" + NC + "CBP VIA DVIDS"),
 VAULT=("FILE FOOTAGE · CBP SEIZED-DRUG VAULT", "SAN DIEGO COUNTY, 2025" + NC + "CBP VIA DVIDS"),
 OFFL=("FILE FOOTAGE · COAST GUARD COCAINE OFFLOAD", "SAN DIEGO, DEC. 2025" + NC + "U.S. COAST GUARD VIA DVIDS"),
 XFER=("FILE FOOTAGE · HSI / FBI FOREIGN TRANSFER OF CUSTODY", "MIAMI, SEPT. 2026" + NC + "ICE / HSI VIA DVIDS"),
)
CL = {
 "NI1": ("1015442", [(116, 128.5), (140, 163), (184, 200), (224, 256)], "NI", {}),
 "NI2": ("1016602", [(32, 44), (68, 84), (92, 108), (116, 136), (144, 156), (160, 184)], "NI", {}),
 "NI3": ("1016334", [(16, 50), (64, 92), (136, 143)], "NI", {}),
 "JNG": ("1015442", [(0.3, 24), (44, 104)], "JNG", {}),
 "JNG2": ("1016602", [(0.3, 28)], "JNG", {}),
 "HELI": ("448156", [(52.5, 66.5)], "HELI", {}),
 "CONV": ("448156", [(76.5, 111)], "CONV", {}),
 "FUER": ("992358", [(0.5, 23), (104, 118), (160, 170)], "FUER", {}),
 "FLAG": ("839841", [(0.3, 3.6)], "FLAG", {}),
 "PAT": ("1028572", [(44.5, 62), (64, 79.5), (100, 106), (116, 160)], "PAT", {}),
 "SEA": ("1005660", [(4, 250)], "SEA", {}),
 "HQ": ("974123", [(4, 11), (13, 40), (48, 149)], "HQ", {}),
 "HSIR": ("1020040", [(4, 106)], "HSIR", {}),
 "RAID": ("860902", [(13, 50), (76, 100)], "RAID", {}),
 "FENT": ("893769", [(12, 118)], "FENT", {}),
 "METH": ("917814", [(4, 100)], "METH", {}),
 "VAULT": ("994254", [(12, 300)], "VAULT", {}),
 "OFFL": ("990363", [(4, 125)], "OFFL", {}),
 "XFER": ("1024394", [(12, 140)], "XFER", {}),
}
POOL = {"MXU": ["NI1", "NI2", "NI3"], "MXW": ["NI3", "NI2", "NI1"], "MXJ": ["JNG", "JNG2", "NI2"], "DIAB": ["HELI", "CONV", "PAT"],
        "DIABX": ["CONV", "HELI", "PAT", "FUER"], "FUER": ["FUER", "NI1"], "FLAG": ["FLAG", "FUER", "NI1"], "PATROL": ["PAT", "CONV"],
        "FBIB": ["SEA", "HQ"], "FBIC": ["SEA", "HQ"], "FBIH": ["HQ", "SEA", "HSIR"], "FENT": ["FENT", "METH", "VAULT", "OFFL"],
        "LAB": ["FENT", "VAULT", "OFFL"], "METH": ["METH", "VAULT", "FENT", "OFFL"], "VAULT": ["VAULT", "OFFL", "FENT"],
        "RAID": ["HSIR", "RAID", "HQ"], "XFER": ["XFER", "HSIR", "HQ"], "CHAPO": ["XFER", "HSIR", "PAT"], "MP": ["HQ", "SEA", "PAT", "FUER"]}
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
    if all(s_[0].startswith("g:") for s_ in shots) and vd[i] + o.get("gap", 0.45) > 10 and not shots[0][0].startswith(("g:chapter", "g:title", "g:end")):
        shots = list(shots) + [("pool:MP", 0, {})]
    pools = [s[0][5:] for s in shots if s[0].startswith("pool:")]
    if not pools: out[i] = (txt, shots, o); continue
    L = vd[i] + o.get("gap", 0.45) + (1.0 if i == 0 else 0)
    fixed = [s_ for s_ in shots if not s_[0].startswith("pool:")]
    npool = len(pools) if fixed else max(len(pools), math.ceil(L / 6.2))
    d = L / (npool + len(fixed)) + 0.25
    order = POOL[pools[0]]; r = rot.get(pools[0], 0); order = order[r:] + order[:r]; rot[pools[0]] = (r + 1) % len(POOL[pools[0]])
    got = None
    FB = ["HQ", "SEA", "PAT", "FUER", "NI2", "NI1", "OFFL", "HSIR"]
    for key in order + [k for k in FB if k not in order]:
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
