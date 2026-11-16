#!/usr/bin/env python3
"""Resolve pool placeholders in episode_src.py into concrete clip shots -> episode.py.
Line length = voice duration + gap (as build_ep.py); a line gets ceil(len/6.2) shots, all from ONE clip family so the
on-screen tag matches the picture. Avoids used_clips.json (start..start+7 s), blackdetect windows and overlaps.
Board pools fall back to Ken Burns stills of the FBI's own Top Ten poster / web page."""
import json, os, re, math, subprocess, importlib.util
EP = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{EP}/../..")
spec = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
T = dict(
 BOARD=E.BOARD, HQ=E.HQ, SNOW=E.SNOW, TRUCK=E.TRUCK, BRIDGE=E.BRIDGE, COKE=E.COKE, RAID=E.RAID, KC=E.KC, HRT=E.HRT, CHAPO=E.CHAPO,
 ATL=("FILE FOOTAGE · AN FBI ATLANTA OPERATION, GEORGIA", "2026 · NOT THIS CASE · FBI VIA DVIDS"),
 JC=("FILE FOOTAGE · FBI / DEA DARKNET TASK FORCE OFFICE", "2025 · NOT THIS CASE · FBI VIA DVIDS"),
 CJ=("FILE FOOTAGE · FBI CRIMINAL JUSTICE INFORMATION SERVICES, W. VA.", "2026 · NOT THIS CASE · FBI VIA DVIDS"),
 SW=("FILE FOOTAGE · SWAT TRAINING HOSTED BY FBI COLUMBIA", "2025 · NOT THIS CASE · U.S. AIR FORCE VIA DVIDS"),
 DR=("FILE FOOTAGE · FBI DRONE TRAINING", "2026 · NOT THIS CASE · FBI VIA DVIDS"),
 PW=("FILE FOOTAGE · FEDERAL AGENTS PROCESS PAPERWORK", "2018 · NOT THIS CASE · ICE VIA DVIDS"),
 POSTER=("FBI TEN MOST WANTED POSTER · RYAN JAMES WEDDING", "MARCH 2025 · FBI B-ROLL VIA DVIDS"),
)
CL = {
 "BP": ("955350", [(21.2, 29.6)], "BOARD", 0),
 "BW": ("955350", [(69.0, 80.6)], "BOARD", 0),
 "BL": ("955350", [(9.0, 20.6), (41.0, 45.0)], "BOARD", 0),
 "BC": ("955350", [(45.0, 52.6)], "BOARD", 0),
 "HQ": ("955350", [(127.0, 158.4)], "HQ", 0),
 "SN": ("994886", [(37, 60), (61, 116), (117, 130.5), (133, 184)], "SNOW", 1),
 "TR": ("746062", [(1, 32), (41, 64), (97, 112.5), (145, 151)], "TRUCK", 1),
 "BR": ("821593", [(13, 36), (45, 53), (57, 80.5)], "BRIDGE", 1),
 "CO": ("1004185", [(1, 64)], "COKE", 1),
 "RA": ("961569", [(1, 50.5), (85, 96), (101, 150)], "RAID", 1),
 "JC": ("961569", [(53, 60.5)], "JC", 1),
 "KC": ("1000381", [(13, 24), (25, 29), (33, 37), (41, 45), (69, 85), (89, 117)], "KC", 1),
 "KU": ("1000381", [(13, 24)], "KC", 1),
 "AT": ("994973", [(5, 40), (53, 104)], "ATL", 1),
 "HR": ("859915", [(5.5, 8.2), (9, 12.6), (29, 32.5), (37, 44.5), (77, 80.5)], "HRT", 1),
 "CH": ("506089", [(11.5, 17.0), (24, 30)], "CHAPO", 1),
 "CJ": ("1021543", [(1, 40)], "CJ", 1),
 "DR": ("1008216", [(66, 91), (96, 121), (171, 186)], "DR", 1),
 "PW": ("585171", [(71, 100), (241, 255.5)], "PW", 1),
 "SW": ("994298", [(29, 40)], "SW", 1),
}
STILL = {"BOARD_POSTER": ["poster"], "BOARD_WEB": ["fbipage", "poster"], "BOARD_WALL": ["counter", "poster"], "BOARD_COUNTER": ["counter"],
         "HQ": ["building", "seal", "poster", "fbipage", "building2"], "HRT": ["building", "seal"], "CHAPO": ["poster", "seal"], "KC_ROOM": ["fbipage"], "RAID": ["seal"], "KC_CUFF": ["poster"], "KC_NIGHT": ["building2"]}
POOL = {
 "BOARD_POSTER": ["BP", "BW", "BL"], "BOARD_WEB": ["BW", "BL", "BP", "DR", "PW"], "BOARD_WALL": ["BL", "BC", "PW", "DR"], "BOARD_COUNTER": ["BC", "BL"],
 "HQ": ["HQ", "CJ", "PW", "DR", "AT", "SW", "KC", "RA"], "SNOW": ["SN"], "TRUCK": ["TR", "BR"], "BRIDGE": ["BR", "TR"], "COKE": ["CO"],
 "RAID": ["RA", "AT", "SW", "KC"], "KC_CUFF": ["KU", "AT", "KC", "SW"], "KC_NIGHT": ["KC", "AT", "SW", "RA"], "KC_ROOM": ["JC", "CJ", "PW", "RA", "AT", "DR"],
 "HRT": ["HR", "DR", "SW", "AT"], "CHAPO": ["CH", "SW", "AT", "DR"],
}
blocked = {}
for u in json.load(open(f"{ROOT}/used_clips.json")):
    blocked.setdefault(str(u["clip"]), []).append((u["start"] - 0.2, u["start"] + 7.0))
for line in open("/home/claude/work/black.txt").read().splitlines():
    if not line[:1].isdigit(): continue
    cid = line.split()[0]
    for a, b in re.findall(r"black_start:([0-9.]+) black_end:([0-9.]+)", line):
        blocked.setdefault(cid, []).append((float(a) - 0.3, float(b) + 0.3))
taken = {}
def free(cid, a, b):
    return all(not (a < y and x < b) for x, y in blocked.get(cid, []) + taken.get(cid, []))
cursor = {}
def take(key, d):
    cid, ranges, tk, lab = CL[key]
    cands = []
    for ra, rb in ranges:
        t = ra
        while t + d <= rb - 0.1:
            cands.append(round(t, 1)); t += 0.5
    c0 = cursor.get(key, 0)
    for s in [x for x in cands if x >= c0] + [x for x in cands if x < c0]:
        if free(cid, s, s + d):
            taken.setdefault(cid, []).append((s, s + d)); cursor[key] = s + d
            return s
    return None

vd = [dur(f"{EP}/vo/raw_{i:02d}.wav") for i in range(1, len(E.LINES) + 1)]
out_lines, problems, stills = [], [], 0
for i, (txt, shots, o) in enumerate(E.LINES):
    pools = [s[0][5:] for s in shots if s[0].startswith("pool:")]
    if not pools:
        out_lines.append((txt, shots, o)); continue
    L = vd[i] + o.get("gap", 0.45) + (1.0 if i == 0 else 0)
    fixed = [s for s in shots if not s[0].startswith("pool:")]
    n = len(shots)
    npool = max(len(pools), math.ceil(L / 6.2) - len(fixed))
    d = L / (npool + len(fixed)) + 0.25
    got = None
    for key in POOL[pools[0]]:
        starts = []
        for _ in range(npool):
            s = take(key, d)
            if s is None: break
            starts.append(s)
        if len(starts) == npool:
            got = key; break
        cid = CL[key][0]
        for s in starts: taken[cid].remove((s, s + d))
    o2 = dict(o)
    if got:
        cid, _, tk, lab = CL[got]
        newshots = [(cid, s, {}) for s in starts] + fixed
        if o.get("tag") in T.values() or "tag" not in o: o2["tag"] = T[tk]
        if lab: o2["lab"] = 1
        else: o2.pop("lab", None)
    elif pools[0] in STILL:
        stills += 1
        opts = STILL[pools[0]]; key = opts[stills % len(opts)]
        newshots = [("img:" + key, 0, {"kb": "in" if stills % 2 else "pan"})] + fixed
        o2["tag"] = T["POSTER"] if key in ("poster", "fbipage") else E.HQ; o2.pop("lab", None)
    else:
        problems.append((i + 1, pools, round(d, 1))); newshots = shots
    out_lines.append((txt, newshots, o2))
print("problems:", problems, "stills:", stills)
src = open(f"{EP}/episode_src.py").read()
head = src[:src.index("LINES = [")]
tail = src[src.index("\ndef _L("):]
body = "LINES = [\n" + "".join(f" ({t!r},\n  {sh!r},\n  {o!r}),\n" for t, sh, o in out_lines) + "]\n"
open(f"{EP}/episode.py", "w").write(head.replace("pool placeholders", "pool placeholders (RESOLVED by alloc.py)") + body + tail)
json.dump(taken, open(f"{EP}/alloc_taken.json", "w"))
# shot-length check
long_shots = [(i + 1, round((vd[i] + o.get("gap", 0.45)) / len(sh), 1)) for i, (t, sh, o) in enumerate(out_lines) if (vd[i] + o.get("gap", 0.45)) / len(sh) > 7.5]
print("shots > 7.5 s:", long_shots)
print("total s", round(sum(vd) + sum(o.get("gap", 0.45) for _, _, o in E.LINES) + 1, 1))
