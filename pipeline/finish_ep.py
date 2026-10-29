#!/usr/bin/env python3
"""Subtitles/overlays (ASS), score + FX + nat sound, final mix.
usage: finish_ep.py <episode_dir> <clips_dir>   (after build_ep.py)"""
import json, os, re, subprocess, sys, importlib.util
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve
EP = os.path.abspath(sys.argv[1]); CLIPS = os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location("episode", os.path.join(EP, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
LINES, DISPLAY = E.LINES, E.DISPLAY
META = getattr(E, "META", {})
os.chdir(EP)

T = json.load(open("timing.json"))
S, V, TOTAL = T["starts"], T["vdur"], T["total"]
SR = 48000
def run(c): subprocess.run(c, check=True)

def disp(t):
    for a, b in DISPLAY: t = t.replace(a, b)
    return t

# ---------------- ASS ----------------
def ts(x):
    x = max(0, x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
def chunks(text, maxc=46):
    out = []
    for s in re.split(r"(?<=[.!?:])\s+", text):
        cur = ""
        for w in s.split():
            if len(cur) + len(w) + 1 > maxc and cur: out.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        if cur: out.append(cur)
    m = []
    for c in out:
        if m and len(c) < 14 and len(m[-1]) + len(c) < maxc + 6: m[-1] += " " + c
        else: m.append(c)
    return m

RED = r"\c&H2D21D3&"
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Oswald Medium,50,&H00DCE7EC,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0.5,0,1,2.6,1.2,2,200,200,64,1
Style: Tag,Oswald,40,&H00DCE7EC,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,4,0,1,0,0,7,110,110,90,1
Style: TagSub,IBM Plex Mono SemiBold,24,&H00898077,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,6,0,1,0,0,7,110,110,90,1
Style: Big,Anton,190,&H00DCE7EC,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,6,5,60,60,60,1
Style: BigSub,Oswald,56,&H003DA3E8,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,8,0,1,2,2,5,60,60,60,1
Style: Credit,IBM Plex Mono SemiBold,22,&H00B8B8B8,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,0,0,2,60,60,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
def add(a, b, st, tx, layer=0): ev.append(f"Dialogue: {layer},{ts(a)},{ts(b)},{st},,0,0,0,,{tx}")
srt, n = [], 1
def srt_t(x): return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{min(999,int(round((x%1)*1000))):03d}"

for i, (txt, shots, o) in enumerate(LINES):
    d_txt = disp(txt)
    cs = chunks(d_txt); tot = sum(len(c) for c in cs); a = S[i]
    is_title = any(s[0] == "g:title" for s in shots)
    for c in cs:
        b = a + V[i] * len(c) / tot
        add(a, b - 0.02, "Sub", r"{\fad(60,60)}" + c)
        srt.append(f"{n}\n{srt_t(a)} --> {srt_t(b)}\n{c}\n"); n += 1
        a = b
    if "tag" in o:
        t1, t2 = o["tag"]; a0, b0 = S[i] + 0.2, S[i] + min(V[i] + 0.3, 6.5)
        bar = r"{\an7\pos(110,92)\fad(250,300)\bord0\shad0\c&H2D21D3&\p1}m 0 0 l 10 0 l 10 74 l 0 74{\p0}"
        add(a0, b0, "Tag", bar, 2)
        add(a0, b0, "Tag", r"{\an7\pos(140,86)\fad(250,300)}" + t1, 2)
        add(a0, b0, "TagSub", r"{\an7\pos(142,136)\fad(250,300)}" + t2, 2)
    if "big" in o:
        t1, t2 = o["big"]; a0, b0 = S[i], S[i] + V[i] + 0.4
        add(a0, b0, "Big", r"{\an5\pos(960,470)\fad(100,300)\t(0,350,\fscx100\fscy100)\fscx115\fscy115}" + t1, 3)
        add(a0 + 0.25, b0, "BigSub", r"{\an5\pos(960,600)\fad(250,300)}" + t2, 3)

# description credit at the very end
e = TOTAL - 4.0
add(e + 0.6, TOTAL, "Credit", r"{\fad(400,0)}" + META.get("credit", "Footage via DVIDS — public domain. Appearance does not imply endorsement."), 5)
open("subs.ass", "w", encoding="utf-8").write(head + "\n".join(ev) + "\n")
open("subs_en.srt", "w", encoding="utf-8").write("\n".join(srt))

# ---------------- AUDIO ----------------
N = int(TOTAL * SR) + SR
t = np.arange(N) / SR
rng = np.random.default_rng(1)
def lp(x, f, o=4): return sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)
def bp(x, a, b): return sosfilt(butter(2, [a, b], "band", fs=SR, output="sos"), x)
irl = int(2.6 * SR)
ir = rng.standard_normal(irl) * np.exp(-np.arange(irl) / (0.55 * SR)); ir = lp(ir, 5000); ir /= np.sqrt(np.sum(ir**2)) * 3

# drone in A minor-ish, slowly evolving per act
drone = np.zeros(N)
for f, a in [(55, .5), (82.41, .3), (110, .18), (130.81, .07), (164.81, .05)]:
    lfo = 0.55 + 0.45 * np.sin(2 * np.pi * (0.021 + f / 12000) * t + f)
    drone += a * lfo * np.sin(2 * np.pi * f * t + 0.25 * np.sin(2 * np.pi * 0.07 * t))
drone += lp(rng.standard_normal(N), 700) * 0.06 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.04 * t))
hi = sum(np.sin(2 * np.pi * f * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.05 * t + k)) for k, f in enumerate([329.63, 349.23]))
drone += lp(hi, 1400) * 0.03
env = np.ones(N) * 0.6
fi = int(2.5 * SR); env[:fi] *= np.linspace(0, 1, fi)
eo = int((TOTAL - 5) * SR); env[eo:] *= np.linspace(1, 0, N - eo)
drone *= env

def thump(amp=1.0, f0=52):
    L = int(.5 * SR); tt = np.arange(L) / SR
    f = f0 * (1 + 1.6 * np.exp(-tt * 30))
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)
# chapter start times
chap = [S[i] for i, (_, sh, _) in enumerate(LINES) if any(s[0] == "g:chapter" for s in sh)]
hunt = chap[3] if len(chap) > 3 else S[0]
crack = chap[5] if len(chap) > 5 else TOTAL
pulse = np.zeros(N)
tt_ = 0.0
while tt_ < TOTAL - 6:
    fast = (hunt <= tt_ < hunt + 70) or (crack <= tt_ < crack + 40) or tt_ < 25
    amp = .55 if fast else .32
    for off, a in [(0, 1), (.22, .55)]:
        i0 = int((tt_ + off) * SR); th = thump(amp * a); pulse[i0:i0 + len(th)] += th[:max(0, min(len(th), N - i0))]
    tt_ += 0.95 if fast else 1.5

def impact(amp=1.0):
    L = int(4 * SR); tt = np.arange(L) / SR
    f = 30 * (1 + 2.6 * np.exp(-tt * 12))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.6) + lp(rng.standard_normal(L), 3000) * np.exp(-tt * 18) * .6
    x = x + fftconvolve(x, ir)[:L] * .8
    return amp * x / np.abs(x).max()
def riser(d=1.6, amp=.4):
    L = int(d * SR); n_ = rng.standard_normal(L + 4000); out = np.zeros(L); seg = SR // 20
    for k in range(0, L, seg):
        fc = 300 + 5200 * (k / L) ** 2
        out[k:k + seg] = bp(n_[k:k + seg + 2000], fc * .7, fc * 1.3)[:len(out[k:k + seg])]
    return amp * out / np.abs(out).max() * (np.arange(L) / L) ** 2
def whoosh(amp=.35):
    L = int(.7 * SR); tt = np.arange(L) / SR
    x = bp(rng.standard_normal(L), 400, 4000) * np.sin(np.pi * tt / tt[-1]) ** 2
    return amp * x / np.abs(x).max()
fx = np.zeros(N)
def put(x, at):
    i0 = int(max(0, at) * SR); j = min(N, i0 + len(x)); fx[i0:j] += x[:j - i0]
put(impact(.8), 0.05)
for i, (_, sh, o) in enumerate(LINES):
    names = [s[0] for s in sh]
    if "g:title" in names: put(riser(1.6, .4), S[i] + V[i] - 1.4); put(impact(1.0), S[i] + V[i] + 0.15)
    if "g:chapter" in names: put(whoosh(.4), S[i] - 0.35); put(impact(.6), S[i] + 0.05)
    if "g:stat" in names or "big" in o: put(impact(.45), S[i] + 0.1)
    if any(n in names for n in ("g:doc_treasury", "g:doc_doj", "g:fto")): put(impact(.5), S[i] + 0.75)
    if "g:end" in names: put(riser(2.0, .35), S[i] - 1.6); put(impact(1.0), S[i] + 0.4)
music = drone * .5 + pulse * .45
music = music + fftconvolve(music, ir[:SR])[:N] * .25

voice = np.zeros(N)
for i, s in enumerate(S):
    x, sr = sf.read(f"vo/l_{i+1:02d}.wav")
    if x.ndim > 1: x = x.mean(1)
    i0 = int(s * SR); voice[i0:i0 + len(x)] += x[:N - i0]
voice = voice + fftconvolve(voice, ir[:int(.6 * SR)])[:N] * .08
venv = np.convolve(np.abs(voice), np.ones(int(.3 * SR)) / int(.3 * SR), mode="same")
duck = 1 - 0.6 * np.clip(venv / (venv.max() * .12 + 1e-9), 0, 1)
music *= duck
sf.write("music.wav", (music / max(1e-9, np.abs(music).max()) * .5).astype(np.float32), SR)
sf.write("fx.wav", (fx / max(1e-9, np.abs(fx).max()) * .6).astype(np.float32), SR)
sf.write("voice.wav", (voice / max(1e-9, np.abs(voice).max()) * .9).astype(np.float32), SR)

# nat sound from clips
os.makedirs("nat", exist_ok=True)
lst = open("nat/list.txt", "w")
for k, sg in enumerate(T["segs"]):
    out = f"nat/{k:03d}.wav"; src = sg["src"]
    if src.startswith("g:") or src.startswith("img:"):
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{sg['d']:.3f}", out])
    else:
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(sg["ss"]), "-i", f"{CLIPS}/{src}.mp4", "-t", f"{sg['d']:.3f}",
             "-af", "aresample=48000,pan=mono|c0=0.5*c0+0.5*c1,apad", "-ac", "1", "-t", f"{sg['d']:.3f}", out])
    lst.write(f"file '{k:03d}.wav'\n")
lst.close()
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "nat/list.txt",
     "-af", "highpass=f=150,lowpass=f=6000,dynaudnorm=f=200:g=15,volume=0.4", "nat.wav"])

run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", "voice.wav", "-i", "music.wav", "-i", "fx.wav", "-i", "nat.wav", "-filter_complex",
     "[0:a]aformat=channel_layouts=stereo,asplit[v1][v2];[1:a]aformat=channel_layouts=stereo,volume=0.5[m];[2:a]aformat=channel_layouts=stereo,volume=0.7[f];"
     "[3:a]aformat=channel_layouts=stereo,volume=0.3[n];[n][v2]sidechaincompress=threshold=0.02:ratio=10:attack=20:release=400[nd];"
     "[v1][m][f][nd]amix=inputs=4:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11",
     "-t", f"{TOTAL:.3f}", "-ar", "48000", "mix.wav"])
print("audio + subs done")
