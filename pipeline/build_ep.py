#!/usr/bin/env python3
"""Render timeline segments for an episode. usage: build_ep.py <episode_dir> <clips_dir>
episode.py must define LINES (see episodes/001-ms13/episode.py) and META (imgs: {key: path}).
Graphics frames must already exist in <ep>/gfx (node graphics.mjs <ep>/gspec.json <ep>/gfx)."""
import json, os, subprocess, sys, glob, hashlib, importlib.util
EP = os.path.abspath(sys.argv[1]); CLIPS = os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
LINES = E.LINES; IMGS = getattr(E, "META", {}).get("imgs", {})
W, H, FPS = 1920, 1080, 30
os.chdir(EP); os.makedirs("seg", exist_ok=True)
def run(c): subprocess.run(c, check=True)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())

vd = []
for i in range(1, len(LINES) + 1):
    raw, out = f"vo/raw_{i:02d}.wav", f"vo/l_{i:02d}.wav"
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(raw):
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", raw, "-af",
             "highpass=f=70,equalizer=f=140:t=q:w=1:g=3,equalizer=f=3200:t=q:w=1.2:g=2,acompressor=threshold=-20dB:ratio=3:attack=4:release=90,loudnorm=I=-16:TP=-1.5",
             "-ar", "48000", "-ac", "2", out])
    vd.append(dur(out))
starts, t = [], 1.0
for i, (txt, shots, o) in enumerate(LINES):
    starts.append(t); t += vd[i] + o.get("gap", 0.45)
TOTAL = t
print("TOTAL", round(TOTAL, 1), flush=True)

GRADE = ("eq=contrast=1.12:saturation=0.74:brightness=-0.02:gamma=0.97,"
         "colorbalance=rs=-0.035:bs=0.045:rh=0.03:bh=-0.03,vignette=angle=PI/4.4,format=yuv420p")
def gkey(name, opts): return name + "_" + hashlib.md5(json.dumps(opts, sort_keys=True).encode()).hexdigest()[:6]
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS)]

def render(idx, shot, d):
    src, ss, o = shot; out = f"seg/{idx:03d}.mp4"; n = max(1, int(round(d * FPS)))
    if src.startswith("g:"):
        key = gkey(src[2:], o); frames = sorted(glob.glob(f"gfx/{key}/f*.jpg")); nint = len(frames)
        vf = (f"[0:v]fps={FPS},trim=end_frame={min(n, nint)},setpts=PTS-STARTPTS[a];"
              f"[1:v]loop=loop=-1:size=1,fps={FPS},trim=end_frame={max(0, n - nint) + 1},setsar=1,setpts=PTS-STARTPTS[b];"  # RULE: graphics hold perfectly still after their intro (no zoom/drift -> no jitter)
              f"[a][b]concat=n=2:v=1,trim=end_frame={n},format=yuv420p,fade=t=in:st=0:d=0.2[v]")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"gfx/{key}/f%04d.jpg",
             "-loop", "1", "-i", frames[-1], "-filter_complex", vf, "-map", "[v]", "-frames:v", str(n), "-an"] + ENC + [out])
    elif src.startswith("img:"):
        img = IMGS[src[4:]]; kb = o.get("kb", "in")
        z = "min(zoom+0.0008,1.22)" if kb == "in" else "1.15"
        x = "iw/2-(iw/zoom/2)" if kb == "in" else f"(iw-iw/zoom)*on/{n}"
        # RULE: Ken Burns only on stills, computed on a 4x-supersampled canvas so motion is sub-pixel smooth
        vf = (f"scale=7680:-2,crop=7680:4320,zoompan=z='{z}':x='{x}':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
              f"eq=saturation=0.6,curves=preset=increase_contrast,{GRADE}")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-i", img, "-vf", vf, "-frames:v", str(n), "-an"] + ENC + [out])
    else:
        clip = f"{CLIPS}/{src}.mp4"; pre = ""
        cd = dur(clip)
        if ss + d > cd - 0.4:  # never run past the end of a clip (end slates / black)
            print(f"WARN clip {src} start {ss} + {d:.1f}s > {cd:.1f}s, clamping", flush=True)
            ss = max(0.0, cd - d - 0.4)
        if o.get("heli"): pre = "crop=iw*0.70:ih*0.70:iw*0.15:ih*0.03,"
        if o.get("pb"): pre = "crop=ih*4/3:ih:(iw-ih*4/3)/2:0,"
        if o.get("crop"): pre = f"crop={o['crop']},"
        # RULE: no artificial zoom/drift on footage (integer-pixel crops/scales make it shake); keep the camera's own motion
        vf = (f"{pre}fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1,{GRADE}")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{ss}", "-i", clip, "-t", f"{d + 0.2:.3f}", "-vf", vf,
             "-frames:v", str(n), "-an"] + ENC + [out])
    return out, n / FPS

segs, files, acc, idx = [], [], 0.0, 0
for i, (txt, shots, o) in enumerate(LINES):
    a = 0.0 if i == 0 else starts[i]; b = starts[i + 1] if i + 1 < len(LINES) else TOTAL
    for j, shot in enumerate(shots):
        d = round((a + (b - a) * (j + 1) / len(shots) - acc) * FPS) / FPS
        f, real = render(idx, shot, d); files.append(f)
        segs.append(dict(t=acc, d=real, src=shot[0], ss=shot[1], line=i)); acc += real; idx += 1
    print(f"line {i+1}/{len(LINES)}", flush=True)
with open("seg/list.txt", "w") as fh:
    for f in files: fh.write(f"file '{os.path.basename(f)}'\n")
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "seg/list.txt", "-c", "copy", "video_raw.mp4"])
json.dump(dict(starts=starts, vdur=vd, total=TOTAL, segs=segs), open("timing.json", "w"), indent=1)
print("done", round(acc, 2))
