#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py (023, from 022/alloc.py).
One clip family per line so the FILE FOOTAGE tag matches the picture; <= 6.2 s per shot; avoids used_clips.json,
blackdetect windows (/home/claude/work/black.txt) and overlaps."""
import json, os, re, math, subprocess, importlib.util
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
NC = " · NOT THIS CASE · "
T = dict(
 P984=("FILE FOOTAGE · CBP OFFICERS SEARCH A VEHICLE, SECONDARY INSPECTION", "SAN YSIDRO, CALIF., 2025" + NC + "CBP VIA DVIDS"),
 P907=("FILE FOOTAGE · CBP NON-INTRUSIVE INSPECTIONS AT A PORT OF ENTRY", "NOGALES, ARIZ., 2023" + NC + "CBP VIA DVIDS"),
 K9=("FILE FOOTAGE · CBP K9 AND BOOTH INSPECTIONS", "SAN YSIDRO, CALIF., 2025" + NC + "CBP VIA DVIDS"),
 CASH=("FILE FOOTAGE · CBP OFFICERS COUNT UNREPORTED CASH", "CHICAGO O'HARE, 2024" + NC + "CBP VIA DVIDS"),
 DRONE=("FILE FOOTAGE · U.S. ARMY COUNTER-DRONE SYSTEM AT THE BORDER", "JTF-SOUTHERN BORDER, 2026" + NC + "U.S. ARMY VIA DVIDS"),
 RCG=("FILE FOOTAGE · COAST GUARD RIVERINE PATROL, RIO GRANDE", "TEXAS, 2026" + NC + "U.S. COAST GUARD VIA DVIDS"),
 RARMY=("FILE FOOTAGE · ARMY CREWS ON THE RIO GRANDE", "TEXAS, 2026" + NC + "U.S. ARMY VIA DVIDS"),
 EP=("FILE FOOTAGE · SOLDIERS + BORDER PATROL, EAGLE PASS STATION", "EAGLE PASS, TEX., 2025" + NC + "U.S. ARMY VIA DVIDS"),
 PAT=("FILE FOOTAGE · SOLDIERS + BORDER PATROL ON THE RIO GRANDE", "TEXAS, 2025" + NC + "U.S. ARMY VIA DVIDS"),
 BPT=("FILE FOOTAGE · U.S. BORDER PATROL AGENTS", "TECATE, CALIF., 2026" + NC + "CBP VIA DVIDS"),
 GUNS=("FILE FOOTAGE · SEIZED SOUTHBOUND WEAPONS ON DISPLAY", "NOGALES, ARIZ., MAY 2025" + NC + "CBP VIA DVIDS"),
 NI=("FILE FOOTAGE · MEXICAN NAVAL INFANTRY + U.S. MARINES, URBAN TRAINING", "RIMPAC 2026, HAWAII" + NC + "U.S. NAVY VIA DVIDS"),
 JNG=("FILE FOOTAGE · U.S. MARINES + MEXICAN NAVAL INFANTRY, FIELD TRAINING", "RIMPAC 2026, HAWAII" + NC + "U.S. NAVY VIA DVIDS"),
 FBI=("FILE FOOTAGE · FBI AGENTS DURING AN ENFORCEMENT SURGE", "BALTIMORE, AUG. 2026" + NC + "FBI VIA DVIDS (FACES BLURRED BY FBI)"),
 HQ=("FILE FOOTAGE · FBI HEADQUARTERS, J. EDGAR HOOVER BUILDING", "WASHINGTON, D.C., 2025 · FBI VIA DVIDS"),
 SRT=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM, WARRANT SERVICE", "2025" + NC + "ICE / HSI VIA DVIDS"),
 HSIR=("FILE FOOTAGE · HSI ENFORCEMENT OPERATION (FACES BLURRED BY HSI)", "OMAHA, NEB., AUG. 2026" + NC + "ICE / HSI VIA DVIDS"),
 RAID=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM, SEARCH WARRANT", "CHICAGO, OCT. 2022" + NC + "ICE / HSI VIA DVIDS"),
 FENT=("FILE FOOTAGE · CBP FENTANYL SEIZURE AT A PORT OF ENTRY", "SAN YSIDRO, CALIF., 2023" + NC + "CBP VIA DVIDS"),
 METH=("FILE FOOTAGE · SEIZED METH, HEROIN AND FENTANYL", "NOGALES, ARIZ., 2023" + NC + "CBP VIA DVIDS"),
 VAULT=("FILE FOOTAGE · CBP SEIZED-DRUG VAULT", "SAN DIEGO COUNTY, 2025" + NC + "CBP VIA DVIDS"),
 PCN=("PRESS CONFERENCE · SAN ANTONIO · NOV. 20, 2026", "U.S. ATTORNEY'S OFFICE, W.D. TEX. · SOURCE: NTD LIVE STREAM"),
 PCF=("PRESS CONFERENCE · SAN ANTONIO · NOV. 20, 2026", "U.S. ATTORNEY'S OFFICE, W.D. TEX. · SOURCE: FORBES BREAKING NEWS"),
)
PC = {"crop": "iw*0.8:ih*0.8:iw*0.1:0", "lab": 0}
CL = {
 "P984": ("984482", [(9, 296)], "P984", {}), "P907": ("907567", [(10, 296)], "P907", {}), "K9": ("989488", [(13, 106)], "K9", {}),
 "CASH": ("943762", [(13, 214)], "CASH", {}),
 "DR1": ("1028963", [(1, 58), (66, 118), (126, 166)], "DRONE", {}), "DR2": ("1022178", [(2, 62)], "DRONE", {}), "DR3": ("1027847", [(40, 50)], "DRONE", {}),
 "RCG1": ("1026422", [(0.5, 64), (70, 138)], "RCG", {}), "RCG2": ("1026652", [(0.5, 38), (86, 104)], "RCG", {}), "RAR": ("995945", [(14, 24), (30, 36), (62, 72)], "RARMY", {}),
 "EP": ("957013", [(0.5, 70)], "EP", {}), "PAT1": ("959446", [(1, 90)], "PAT", {}), "PAT2": ("952317", [(1, 70)], "PAT", {}), "BPT": ("1027829", [(13, 148)], "BPT", {}),
 "GUNS": ("960896", [(14, 50), (60, 88)], "GUNS", {}),
 "NI1": ("1015442", [(116, 128.5), (140, 163), (184, 200), (224, 256)], "NI", {}),
 "NI2": ("1016602", [(32, 44), (68, 84), (92, 108), (116, 136), (144, 156), (160, 184)], "NI", {}),
 "NI3": ("1016334", [(16, 50), (64, 92), (136, 143)], "NI", {}),
 "JNG": ("1015442", [(0.3, 24), (44, 104)], "JNG", {}), "JNG2": ("1016602", [(0.3, 28)], "JNG", {}),
 "FBI": ("1018364", [(10, 138)], "FBI", {}), "HQ": ("974123", [(4, 11), (13, 40), (48, 149)], "HQ", {}),
 "SRT": ("950625", [(8, 260)], "SRT", {}), "HSIR": ("1020040", [(4, 106)], "HSIR", {}), "RAID": ("860902", [(13, 50), (76, 100)], "RAID", {}),
 "FENT": ("893769", [(12, 118)], "FENT", {}), "METH": ("917814", [(4, 100)], "METH", {}), "VAULT": ("994254", [(12, 300)], "VAULT", {}),
}
for n in "abcdefghij": CL["N" + n] = ("ntd_" + n, [(0.5, 89.5)], "PCN", PC)
for n in "ab": CL["F" + n] = ("fbn_" + n, [(0.5, 89.5)], "PCF", PC)
PRESSK = ["N" + n for n in "abcdefghij"] + ["Fa", "Fb"]
POOL = {"PORT": ["P984", "P907", "K9"], "CASH": ["CASH"], "DRONE": ["DR1", "DR2", "DR3"], "RIVER": ["RCG1", "RCG2", "RAR"],
        "BORDER": ["EP", "PAT1", "PAT2", "BPT"], "GUNS": ["GUNS", "P984"], "MXF": ["NI1", "NI2", "NI3", "JNG", "JNG2"],
        "FBI": ["FBI", "HQ"], "RAID": ["SRT", "HSIR", "RAID", "FBI"], "LAB": ["FENT", "METH", "VAULT"], "PRESS": PRESSK, "MP": ["P907", "EP", "RCG1", "FBI"]}
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
    FB = ["EP", "PAT1", "RCG1", "P907", "NI2", "NI1", "FBI", "HSIR"]
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
        it = iter(starts); newsh = [s_ if not s_[0].startswith("pool:") else (cid, next(it), dict({"lab": 1}, **so)) for s_ in shots]
        newsh += [(cid, x, dict({"lab": 1}, **so)) for x in it]
        o3 = dict(o2) if (fixed or "tag" in o2) else dict(o2, tag=T[tk], lab=so.get("lab", 1))
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
