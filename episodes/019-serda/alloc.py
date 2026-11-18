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
 AT=("FILE FOOTAGE · FBI ATLANTA TEAMS STAGE FOR AN ARREST OPERATION", "GLYNN COUNTY, GA., FEB. 2026" + NC + "FBI VIA DVIDS"),
 YB=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM, NIGHT OPERATION", "SAN JUAN, P.R., SEPT. 2023" + NC + "ICE / HSI VIA DVIDS"),
 KC1=("FILE FOOTAGE · FBI-LED OPERATION SPRING CLEANING", "SOUTHWEST MISSOURI, MARCH 2026" + NC + "FBI VIA DVIDS"),
 TUC=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM SERVES A WARRANT", "TUCSON, ARIZ., NOV. 2016" + NC + "ICE / HSI VIA DVIDS"),
 RC=("FILE FOOTAGE · FBI-LED OPERATION RED CARD", "KANSAS CITY, MAY 2026" + NC + "FBI VIA DVIDS"),
 BA1=("FILE FOOTAGE · FBI ARREST OPERATION", "BALTIMORE, FEB. 2026" + NC + "FBI VIA DVIDS"),
 BA2=("FILE FOOTAGE · FBI ARREST OPERATION", "BALTIMORE, FEB. 2026" + NC + "FBI VIA DVIDS"),
 PHX=("FILE FOOTAGE · HSI AGENTS SERVE A SEARCH WARRANT", "PHOENIX, JUNE 2023" + NC + "ICE / HSI VIA DVIDS"),
 LA=("FILE FOOTAGE · HSI AGENTS SERVE A SEARCH WARRANT", "LOS ANGELES, FEB. 2022" + NC + "ICE / HSI VIA DVIDS"),
 COL=("FILE FOOTAGE · FBI ARREST OPERATION", "COLUMBIA, S.C., MAY 2025" + NC + "FBI VIA DVIDS"),
 GM=("FILE FOOTAGE · SEIZED FENTANYL PILLS, HSI OPERATION GHOST MILL", "TUCSON, JAN. 2023" + NC + "ICE / HSI VIA DVIDS"),
 VLT=("FILE FOOTAGE · CBP SEIZED-PROPERTY VAULT", "SAN DIEGO COUNTY, NOV. 2025" + NC + "CBP VIA DVIDS"),
 NOG=("FILE FOOTAGE · FENTANYL SEIZED BY CBP", "NOGALES, ARIZ., NOV. 2023" + NC + "CBP VIA DVIDS"),
 SY=("FILE FOOTAGE · CBP PROCESSES SEIZED FENTANYL", "SAN YSIDRO, CALIF., 2017" + NC + "CBP VIA DVIDS"),
 CR=("FILE FOOTAGE · CBP FENTANYL INTERDICTION", "2022" + NC + "CBP VIA DVIDS"),
 KCC=("FILE FOOTAGE · FBI COMMAND POST", "MISSOURI, MARCH 2026" + NC + "FBI VIA DVIDS"),
 LAB=("FILE FOOTAGE · HSI EVIDENCE PROCESSING", "PHOENIX, JUNE 2023" + NC + "ICE / HSI VIA DVIDS"),
 IB=("FILE FOOTAGE · HSI SPECIAL RESPONSE TEAM BRIEFING", "TEXAS, AUG. 2018" + NC + "ICE / HSI VIA DVIDS"),
 ERT=("FILE FOOTAGE · FBI EVIDENCE RESPONSE TEAM TRAINING", "MAY 2024" + NC + "U.S. ARMY SOUTH VIA DVIDS"),
 SH=("FILE FOOTAGE · FBI TEAMS BRIEF BEFORE ARRESTS, SUMMER HEAT 2.0", "BALTIMORE, AUG. 2026" + NC + "FBI VIA DVIDS"),
)
CL = {
 "AT": ("994973", [(4, 7.5), (12, 35), (44, 63), (68, 83)], "AT", {}),
 "YB": ("899361", [(12.5, 35), (40, 56), (64, 100), (120, 160)], "YB", {}),
 "KC1": ("1000368", [(33.5, 39.5), (84, 96), (111, 116.4)], "KC1", {}),
 "TUC": ("490825", [(4.5, 11), (24, 31), (32, 43.5), (48, 58), (64, 82), (88, 95.5), (124, 131), (136, 143), (160, 169.5)], "TUC", {}),
 "RC": ("1006229", [(15.5, 23.5), (44, 51)], "RC", {}),
 "BA1": ("996734", [(3, 50), (64, 80)], "BA1", {}),
 "BA2": ("996735", [(16, 60), (72, 99), (128, 142)], "BA2", {}),
 "PHX": ("887275", [(24, 68), (76, 88)], "PHX", {}),
 "LA": ("830771", [(4, 27), (36, 47)], "LA", {}),
 "COL": ("963680", [(4, 7.5), (20, 31), (36, 55)], "COL", {}),
 "GM": ("937725", [(36, 50.5)], "GM", {}),
 "VLT": ("994254", [(12, 39), (48, 83), (112, 119), (124, 131), (132, 195)], "VLT", {}),
 "NOG": ("917814", [(4, 47), (48, 83), (92, 99)], "NOG", {}),
 "SY": ("893911", [(12, 35), (40, 55), (96, 160), (164, 190)], "SY", {}),
 "CR": ("870868", [(40, 79), (92, 99)], "CR", {}),
 "KCC": ("1000368", [(104, 111), (52, 59)], "KCC", {}),
 "LAB": ("887275", [(108, 124)], "LAB", {}),
 "IB": ("621697", [(4, 43)], "IB", {}),
 "ERT": ("923153", [(2, 58), (64, 100), (104, 134), (140, 190)], "ERT", {}),
 "SH": ("1018364", [(8, 58), (60, 87), (100, 115), (124, 137)], "SH", {}),
}
POOL = {"DAWN": ["AT", "YB", "SH", "KC1", "TUC"], "RAID": ["TUC", "RC", "BA1", "BA2", "AT", "YB"], "SQUAD": ["PHX", "SH", "LA", "COL", "IB", "BA1", "ERT", "BA2", "YB"],
        "SEARCH": ["PHX", "LA", "GM", "VLT", "TUC", "ERT", "SY"], "EVID": ["NOG", "SY", "VLT", "CR", "GM"], "NIGHT": ["COL", "PHX", "LA", "BA2", "SH", "BA1"],
        "COURT": ["ERT", "KCC", "LAB", "IB", "COL", "SH"]}
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
