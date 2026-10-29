#!/usr/bin/env python3
"""Vertical Shorts cut from a finished episode.
usage: shorts.py <episode_dir> <out_dir>
episode.META["shorts"] = [{"id": "s1", "lines": [first, last], "hook": "TEXT<br>TEXT"}]  (1-indexed line numbers)
Needs video_raw.mp4, mix.wav, timing.json in the episode dir."""
import json, os, re, subprocess, sys, importlib.util
EP = os.path.abspath(sys.argv[1]); OUT = os.path.abspath(sys.argv[2]); os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
T = json.load(open(f"{EP}/timing.json")); S, V = T["starts"], T["vdur"]
def disp(t):
    for a, b in E.DISPLAY: t = t.replace(a, b)
    return t
def ts(x): x = max(0, x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
def words_chunks(text, n=3):
    w = text.split(); return [" ".join(w[i:i + n]) for i in range(0, len(w), n)]
HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,Anton,104,&H00DCE7EC,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,0,6,8,60,60,190,1
Style: Cap,Anton,88,&H00DCE7EC,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,5,0,5,60,60,0,1
Style: Brand,Anton,46,&H00DCE7EC,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,0,0,2,60,60,120,1
Style: CTA,Oswald,54,&H003DA3E8,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,4,0,1,3,0,5,60,60,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for sh in E.META.get("shorts", []):
    a, b = sh["lines"][0] - 1, sh["lines"][1] - 1
    t0 = max(0, S[a] - 0.25); t1 = S[b] + V[b] + 0.6; D = t1 - t0
    ev = []
    hook = sh["hook"].replace("<br>", r"\N")
    hook = re.sub(r"\[(.+?)\]", r"{\\c&H2D21D3&}\1{\\c&HDCE7EC&}", hook)
    ev.append(f"Dialogue: 2,{ts(0)},{ts(D)},Hook,,0,0,0,,{{\\fad(150,0)}}{hook}")
    ev.append(f"Dialogue: 2,{ts(0)},{ts(D)},Brand,,0,0,0,,COLD {{\\3c&H2D21D3&\\bord8}}WARRANT")
    for i in range(a, b + 1):
        txt = disp(E.LINES[i][0]); cs = words_chunks(txt, 3); tot = sum(len(c) for c in cs); s = S[i] - t0
        for c in cs:
            e = s + V[i] * len(c) / tot
            ev.append(f"Dialogue: 1,{ts(s)},{ts(e - 0.01)},Cap,,0,0,0,,{{\\an5\\pos(540,1390)\\fscx92\\fscy92\\t(0,90,\\fscx100\\fscy100)}}{c.upper()}")
            s = e
    ev.append(f"Dialogue: 3,{ts(D - 2.4)},{ts(D)},CTA,,0,0,0,,{{\\an5\\pos(540,1600)\\fad(200,0)}}FULL CASE FILE ON THE CHANNEL")
    ass = f"{OUT}/{sh['id']}.ass"; open(ass, "w", encoding="utf-8").write(HEAD + "\n".join(ev) + "\n")
    vf = (f"[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.25[bg];"
          f"[b]scale=1220:-2,crop=1080:ih[fg];[bg][fg]overlay=0:(H-h)/2-80,ass={ass},fade=t=in:st=0:d=0.3,fade=t=out:st={D-0.5:.2f}:d=0.5[v]")
    out = f"{OUT}/{sh['id']}.mp4"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-t", f"{D:.3f}", "-i", f"{EP}/video_raw.mp4",
                    "-ss", f"{t0:.3f}", "-t", f"{D:.3f}", "-i", f"{EP}/mix.wav", "-filter_complex", vf, "-map", "[v]", "-map", "1:a",
                    "-af", f"afade=t=in:d=0.2,afade=t=out:st={D-0.6:.2f}:d=0.6", "-c:v", "libx264", "-preset", "medium", "-crf", "21",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], check=True)
    print(sh["id"], round(D, 1), "s", out, flush=True)
