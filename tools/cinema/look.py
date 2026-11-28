#!/usr/bin/env python3
"""Doc Cinema — picture tools for long documentaries (ffmpeg only, runs anywhere, no GPU).

  look.py move   IMG OUT.mp4 --dur 5 [--from 1.0 --to 1.18] [--pan left|right|up|down|none] [--fps 30] [--size 1920x1080]
      Camera move on a still with weight: ease-in-out (smoothstep), never linear; slight hand-held drift.
  look.py finish IN.mp4 OUT.mp4 [--grain 6] [--vignette 0.18] [--warm 0.03] [--ca 1]
      Film finish for the whole master: soft grain, vignette, gentle contrast/colour, 1 px chromatic edge.
  look.py join A.mp4 B.mp4 OUT.mp4 --kind whip|dip|wipe|glitch|dissolve [--at SECONDS_FROM_END_OF_A] [--d 0.5]
      Transitions with intent: whip (hblur, fast scene change), dip (to black, time jump), wipe (map/timeline),
      glitch (pixelize, digital/evidence), dissolve (same place, time passing).
Rules (see RULES.md): nothing on screen sits still > 6 s; every move has a reason (reveal, follow, emphasise);
3 layers in frame where possible; grain 2–4 %, vignette 10–20 % in corners, bloom only from real lights.
"""
import argparse, json, subprocess, sys


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-800:])


def probe_dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))


def move(a):
    W, H = map(int, a.size.split("x"))
    n = int(a.dur * a.fps)
    # smoothstep progress s(on) in [0,1]; zoom eased between --from and --to
    s = f"(3*pow(on/{max(n - 1, 1)},2)-2*pow(on/{max(n - 1, 1)},3))"
    z = f"({a.zfrom}+({a.zto}-{a.zfrom})*{s})"
    px = {"left": f"(0.7-0.4*{s})", "right": f"(0.3+0.4*{s})"}.get(a.pan, "0.5")   # 0 = left edge, 1 = right edge
    py = {"up": f"(0.7-0.4*{s})", "down": f"(0.3+0.4*{s})"}.get(a.pan, "0.5")
    x = f"(iw-iw/zoom)*{px}+iw*0.003*sin(on/23)"      # tiny hand-held drift, never a dead frame
    y = f"(ih-ih/zoom)*{py}+ih*0.002*sin(on/31)"
    vf = (f"scale={W * 4}:{H * 4}:force_original_aspect_ratio=increase,crop={W * 4}:{H * 4},"
          f"zoompan=z='{z}':x='{x}':y='{y}':d={n}:s={W}x{H}:fps={a.fps},format=yuv420p")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-i", a.img, "-vf", vf, "-frames:v", str(n),
         "-c:v", "libx264", "-crf", "17", "-preset", "medium", a.out])


def finish(a):
    vf = (f"eq=contrast=1.06:saturation=1.05:gamma=0.98,"
          f"colorbalance=rs={a.warm}:gs=0:bs={-a.warm}:rh={a.warm / 2}:bh={-a.warm / 2},"
          f"rgbashift=rh={a.ca}:bh={-a.ca},"
          f"vignette=angle=PI/4.5:mode=forward:eval=init,"
          f"noise=alls={a.grain}:allf=t+u,format=yuv420p")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", a.inp, "-vf", vf, "-c:v", "libx264", "-crf", "17", "-preset", "medium",
         "-c:a", "copy", "-movflags", "+faststart", a.out])


def join(a):
    kind = {"whip": "hblur", "dip": "fadeblack", "wipe": "wipeleft", "glitch": "pixelize", "dissolve": "dissolve"}[a.kind]
    off = probe_dur(a.a) - (a.at if a.at is not None else a.d)
    fc = f"[0:v][1:v]xfade=transition={kind}:duration={a.d}:offset={off:.3f},format=yuv420p[v]"
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", a.a, "-i", a.b, "-filter_complex", fc, "-map", "[v]",
         "-c:v", "libx264", "-crf", "17", a.out])


p = argparse.ArgumentParser(); sp = p.add_subparsers(dest="cmd", required=True)
m = sp.add_parser("move"); m.add_argument("img"); m.add_argument("out"); m.add_argument("--dur", type=float, default=5)
m.add_argument("--from", dest="zfrom", type=float, default=1.0); m.add_argument("--to", dest="zto", type=float, default=1.15)
m.add_argument("--pan", default="none"); m.add_argument("--fps", type=int, default=30); m.add_argument("--size", default="1920x1080")
f = sp.add_parser("finish"); f.add_argument("inp"); f.add_argument("out"); f.add_argument("--grain", type=float, default=6)
f.add_argument("--vignette", type=float, default=0.18); f.add_argument("--warm", type=float, default=0.03); f.add_argument("--ca", type=int, default=1)
j = sp.add_parser("join"); j.add_argument("a"); j.add_argument("b"); j.add_argument("out"); j.add_argument("--kind", default="dissolve")
j.add_argument("--at", type=float); j.add_argument("--d", type=float, default=0.5)
a = p.parse_args()
{"move": move, "finish": finish, "join": join}[a.cmd](a)
print("ok", a.cmd)
