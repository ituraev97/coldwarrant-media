#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py (021, from 020/alloc.py).
One clip family per line so the FILE FOOTAGE tag matches the picture; <= 6.2 s per shot; avoids used_clips.json,
blackdetect windows (/home/claude/work/black.txt) and overlaps."""
import json, os, re, math, subprocess, importlib.util
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
NC = " · NOT THIS CASE · "
T = dict(
 CELL=("FILE FOOTAGE · AN EMPTY CELL, MILITARY CORRECTIONAL FACILITY", "FORT LEAVENWORTH, KAN., 2012" + NC + "U.S. ARMY VIA DVIDS"),
 JEXT=("FILE FOOTAGE · MILITARY CORRECTIONAL FACILITY", "FORT LEAVENWORTH, KAN., 2012" + NC + "U.S. ARMY VIA DVIDS"),
 JREC=("FILE FOOTAGE · RECREATION YARD BEHIND PRISON FENCES", "FORT LEAVENWORTH, KAN., 2012" + NC + "U.S. ARMY VIA DVIDS"),
 VISIT=("FILE FOOTAGE · A PRISON VISITATION ROOM", "FORT LEAVENWORTH, KAN., 2012" + NC + "U.S. ARMY VIA DVIDS"),
 MSP=("FILE FOOTAGE · MONTANA STATE PRISON", "DEER LODGE, MONT., 2020" + NC + "MONTANA NATIONAL GUARD VIA DVIDS"),
 K9=("FILE FOOTAGE · CALIFORNIA CORRECTIONS (CDCR) K-9 TRAINING", "TRAVIS AFB, CALIF., APRIL 2021" + NC + "U.S. AIR FORCE VIA DVIDS"),
 BRIG=("FILE FOOTAGE · NAVAL BRIG PEARL HARBOR", "HAWAII, 2019" + NC + "U.S. NAVY VIA DVIDS"),
 MOVE=("FILE FOOTAGE · ARMY CORRECTIONS EXERCISE · SOLDIERS PLAY PRISONERS", "SEMBACH, GERMANY, FEB. 2025" + NC + "U.S. ARMY VIA DVIDS"),
 MOVE2=("FILE FOOTAGE · ARMY CORRECTIONS EXERCISE · SOLDIERS PLAY PRISONERS", "SEMBACH, GERMANY, FEB. 2025" + NC + "U.S. ARMY VIA DVIDS"),
 ESC=("FILE FOOTAGE · ESCAPED-INMATE EXERCISE (ARMY, FBI, BOP)", "FORT LEAVENWORTH, KAN., 2022" + NC + "U.S. ARMY VIA DVIDS"),
 SF=("FILE FOOTAGE · HSI GANG OPERATION, PREDAWN WARRANTS", "SAN FRANCISCO, 2012" + NC + "ICE / HSI VIA DVIDS"),
 SJ=("FILE FOOTAGE · ICE ARRESTS, OPERATION CROSS CHECK", "SANTA CLARA COUNTY, CALIF., 2011" + NC + "ICE VIA DVIDS"),
 SHF=("FILE FOOTAGE · HSI GANG OPERATION PROJECT SHADOWFIRE", "ORANGE COUNTY, CALIF., 2016" + NC + "ICE / HSI VIA DVIDS"),
 HON=("FILE FOOTAGE · HSI SEARCH WARRANTS", "HONOLULU, 2019" + NC + "ICE / HSI VIA DVIDS"),
 METH=("FILE FOOTAGE · SEIZED METH, HEROIN AND FENTANYL", "NOGALES, ARIZ., 2023" + NC + "CBP VIA DVIDS"),
 AUR=("FILE FOOTAGE · ICE DETENTION FACILITY (NOT A PRISON)", "AURORA, COLO., 2019" + NC + "ICE VIA DVIDS"),
 AURP=("FILE FOOTAGE · PHONES INSIDE AN ICE DETENTION FACILITY", "AURORA, COLO., 2019" + NC + "ICE VIA DVIDS"),
 PRAI=("FILE FOOTAGE · ICE DETENTION CENTER (NOT A PRISON)", "ALVARADO, TEX., 2017" + NC + "ICE VIA DVIDS"),
 PRAIP=("FILE FOOTAGE · PHONES IN AN ICE DETENTION CENTER", "ALVARADO, TEX., 2017" + NC + "ICE VIA DVIDS"),
 PISA=("FILE FOOTAGE · ICE DETENTION CENTER (NOT A PRISON)", "LOS FRESNOS, TEX., 2017" + NC + "ICE VIA DVIDS"),
 PISAP=("FILE FOOTAGE · PHONES IN AN ICE DETENTION CENTER", "LOS FRESNOS, TEX., 2017" + NC + "ICE VIA DVIDS"),
 VAULT=("FILE FOOTAGE · CBP SEIZED-DRUG VAULT", "SAN DIEGO COUNTY, 2025" + NC + "CBP VIA DVIDS"),
)
CL = {
 "CELL": ("140047", [(75.5, 132), (136, 177), (181, 190)], "CELL", {}),
 "JEXT": ("140047", [(14, 61)], "JEXT", {}),
 "JREC": ("140047", [(192.5, 233), (248, 310)], "JREC", {}),
 "VISIT": ("140047", [(323, 356)], "VISIT", {}),
 "MSP": ("776072", [(12.3, 16), (20, 24), (76, 80), (116, 131), (180, 184)], "MSP", {}),
 "K9": ("794755", [(4, 8), (12, 16), (24, 38), (48, 55), (84, 92), (108, 116)], "K9", {}),
 "BRIG": ("673522", [(4, 11.5), (20, 31), (52, 59), (134, 143)], "BRIG", {}),
 "MOVE": ("960481", [(1, 50), (52, 150), (154, 212)], "MOVE", {}),
 "MOVE2": ("960480", [(16, 48)], "MOVE2", {}),
 "ESC": ("847952", [(36, 60), (84, 92), (140, 152)], "ESC", {}),
 "SF": ("143045", [(8, 150)], "SF", {}),
 "SJ": ("139097", [(13, 75), (80, 300)], "SJ", {}),
 "SHF": ("456015", [(8.5, 230)], "SHF", {}),
 "HON": ("709501", [(8, 130)], "HON", {}),
 "METH": ("917814", [(4, 100)], "METH", {}),
 "AUR": ("701993", [(8.5, 19.5), (176, 182), (184, 212)], "AUR", {}),
 "AURP": ("701993", [(108.5, 116), (258, 268)], "AURP", {}),
 "PRAI": ("505426", [(30.5, 58), (64.5, 84), (136, 170), (204, 215), (224, 232), (254, 276), (296, 316), (324, 352), (354, 374)], "PRAI", {}),
 "PRAIP": ("505426", [(170.5, 178)], "PRAIP", {}),
 "PISA": ("524999", [(4.5, 18), (26.5, 38), (216, 227), (232, 264), (304, 312)], "PISA", {}),
 "PISAP": ("524999", [(264, 272)], "PISAP", {}),
 "VAULT": ("994254", [(12, 300)], "VAULT", {}),
}
POOL = {"PRISON": ["CELL", "PISA", "PRAI", "JEXT", "AUR", "K9", "JREC", "BRIG", "MSP", "AURP", "CELL", "MOVE", "ESC"], "NIGHT": ["PISA", "CELL", "PRAI", "JREC", "AUR", "BRIG", "JEXT", "MOVE", "MSP"],
        "MP": ["MOVE", "PISA", "PRAI", "MOVE2", "ESC", "VISIT", "MOVE"], "RAID": ["SF", "SJ", "SHF", "HON"], "DRUGS": ["METH", "VAULT"], "VISITP": ["VISIT", "BRIG"], "K9P": ["K9", "PISAP", "PRAIP", "AURP", "CELL", "MSP"], "CELLP": ["CELL", "PRAI", "AUR", "JEXT"]}
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
    FB = ["PISA", "PRAI", "AUR", "MOVE", "MOVE2", "CELL", "JEXT", "JREC", "MSP", "BRIG", "ESC", "VISIT"]
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
