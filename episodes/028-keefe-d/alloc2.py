#!/usr/bin/env python3
"""028: replace pool/graphic placeholders with REAL footage ranges (owner: no graphics, real frames). Only title/chapter/end cards stay."""
import importlib.util, os, math, re, soundfile as sf, sys
EP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, EP)
from respell import respell
sp = importlib.util.spec_from_file_location("src", f"{EP}/episode_src.py"); E = importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
POOL = {
 "VER": [("ver1",24,90),("ver4",6,90),("ver2",0,90),("ver3",0,60)],
 "SEN": [("sen1",0,90),("sen3",0,90),("sen2",6,77)],
 "OPEN": [("open1",36,90),("open3",24,90),("open2",60,90),("open2",0,18)],
 "PC": [("pc1",0,90),("pc2",0,90),("pc3",24,90),("pc4",48,90)],
 "RAID": [("raid3",0,90),("body1",18,90),("body2",0,24)],
}
# explicit real-footage ranges per line number (1-based): list of (clip,start,end)
EXPL = {
 8:[("open2",18,24)], 9:[("open2",24,30)], 10:[("open2",30,45)], 11:[("open2",45,51)], 12:[("open2",51,60)],
 13:[("pc4",30,48)], 14:[("pc4",6,30)], 18:[("pc3",12,18),("pc4",24,30)], 23:[("pc4",0,6),("pc4",48,60)],
 28:[("body2",36,48)], 30:[("pc1",60,90)], 35:[("raid3",30,90)], 39:[("pc3",24,60)],
 36:[("raid3",0,30)],
}
TAGS = {
 1:("COURTROOM VIDEO · VERDICT · AUG. 31, 2026","VIA ABC7 AND LAW&CRIME"),
 5:("COURTROOM VIDEO · SENTENCING HEARING","VIA LAW&CRIME, CNN AND AP"),
 8:("ARCHIVE · MGM GRAND · SEPT. 7, 1996","COURT EXHIBITS AND BROADCAST FILE VIA LAW&CRIME"),
 13:("LVMPD NEWS CONFERENCE GRAPHICS · SEPT. 29, 2023","VIA LAW&CRIME"),
 22:("LVMPD NEWS CONFERENCE · SEPT. 29, 2023","VIA LAW&CRIME"),
 34:("POLICE BODY CAMERA · HENDERSON, JULY 2023","LVMPD VIA KTNV AND NEWSNATION"),
 44:("OPENING STATEMENTS · AUG. 2026","COURTROOM VIDEO VIA LAW&CRIME"),
 50:("COURTROOM VIDEO · VERDICT · AUG. 31, 2026","VIA ABC7 AND LAW&CRIME"),
 54:("COURTROOM VIDEO · SENTENCING · OCT. 13, 2026","VIA LAW&CRIME, CNN AND AP"),
}
MANUAL = {8:[("open2",18),("open2",22.5),("open2",26.5)], 9:[("open2",25.5),("open2",29.5)], 10:[("open2",32),("open2",38),("open2",44)],
          11:[("open2",46),("open2",50.5)], 12:[("open2",54),("open2",59.5)]}
used = {}
def free(c,a,b): return all(not(a < y+0.5 and x-0.5 < b) for x,y in used.get(c,[]))
def take(c,lo,hi,d):
    t = lo
    while t + d <= hi - 0.2:
        if free(c,t,t+d): used.setdefault(c,[]).append((t,t+d)); return round(t,1)
        t += 0.5
    return None
rot = {}
out = []
for i,(txt,shots,o) in enumerate(E.LINES,1):
    o = dict(o)
    n = len(E.LINES)
    kinds = [s[0] for s in shots]
    real = [s for s in shots if s[0].startswith("g:") and s[0][2:] in ("title","chapter","end")]
    if real:
        out.append((respell(txt), shots, o)); continue
    raw = sf.read(f"{EP}/vo/raw_{i:02d}.wav"); vd = len(raw[0])/raw[1]
    o["gap"] = round(o.get("gap",0.45) + 0.3, 2)
    L = vd + o["gap"]
    n = max(1, math.ceil(L/5.5)); d = L/n + 0.25
    pool = None
    if i in EXPL:
        ranges = list(EXPL[i]) + [(c,max(0,lo-6),hi+12) for c,lo,hi in EXPL[i]] + POOL["PC"]
    else:
        name = None
        for s in shots:
            if s[0].startswith("pool:"): name = s[0][5:]
        if name is None:  # was a graphic/img line -> map by content
            name = {12:"OPEN",14:"PC",18:"PC",23:"PC",30:"PC",35:"RAID",43:"OPEN",45:"OPEN",55:"SEN",59:"SEN"}.get(i,"PC")
        name = {'BODY':'RAID'}.get(name,name); ranges = POOL[name]; k = rot.get(name,0); ranges = ranges[k:]+ranges[:k]; rot[name] = (k+1) % len(POOL[name])
    starts = []
    for _ in range(0 if i in MANUAL else n):
        got = None
        for c,lo,hi in ranges:
            s = take(c,lo,hi,d)
            if s is not None: got = (c,s); break
        if got is None: print("PROBLEM line",i,d); got = (ranges[0][0], ranges[0][1])
        starts.append(got)
    if i in MANUAL: starts = MANUAL[i]
    sh = [(c,s,{}) for c,s in starts]
    if i in TAGS: o["tag"] = TAGS[i]
    out.append((respell(txt), sh, o))
src = open(f"{EP}/episode_src.py").read()
head = src[:src.index("LINES = [")]; tail = src[src.index("\ndef _L("):]
body = "LINES = [\n" + "".join(f" ({t!r},\n  {sh!r},\n  {o!r}),\n" for t,sh,o in out) + "]\n"
head = head.replace("pool placeholders","pool placeholders (RESOLVED by alloc2.py)")
open(f"{EP}/episode.py","w").write(head+body+tail)
tot = 1+sum(len(sf.read(f"{EP}/vo/raw_{i:02d}.wav")[0])/sf.read(f"{EP}/vo/raw_{i:02d}.wav")[1] + o.get("gap",0.45) for i,(t,s,o) in enumerate(out,1))
print("total min", round(tot/60,2))
