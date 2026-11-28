#!/usr/bin/env python3
"""Doc Cinema — automatic sound design for a LONG documentary (any length), built from real recordings.

usage:
  sound_design.py --voice narration.wav --events events.json --library LIB_DIR --out OUT_DIR
                  [--ambience amb_desert] [--music music_tension] [--seed 7]

events.json — the "event log" the pipeline writes while building the edit (times in seconds of the final video):
  {"duration": 812.4, "events": [
     {"t": 0.0,   "type": "open"},                 # cold open: ambience + music start
     {"t": 41.2,  "type": "chapter"},              # chapter card / big scene change → whoosh (peak on t) + music lift
     {"t": 95.0,  "type": "reveal", "strength": 1},# key reveal → 4–8 s riser ending 0.3 s BEFORE t, short near-silence, impact ON t
     {"t": 130.4, "type": "number"},               # number/stat pops on screen → small hit
     {"t": 150.0, "type": "doc"},                  # document/paper on screen → paper
     {"t": 151.2, "type": "stamp"}, {"t": 170.0, "type": "photo"}, {"t": 200.0, "type": "glitch"},
     {"t": 260.0, "type": "cut", "ambience": "amb_ocean"}   # place change → ambience crossfade (starts 0.4 s early)
  ]}
Five layers (atmosphere, actions, movement, accents, music) — ambience never stops, music is ducked 8 dB under the voice
and 6–10 dB under impacts, every sound has a real onset + fades, repeats are varied (pitch ±3–6 %, gain ±1.5 dB),
one shared room reverb, final −14 LUFS / −1 dBTP. Writes OUT/mix.wav, OUT/stems/{voice,music,ambience,sfx}.wav,
OUT/sound_qa.json (+ waveform/spectrum PNGs) and OUT/credits.txt (CC BY lines for the description).
"""
import argparse, json, os, random, subprocess
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve, resample_poly

SR = 48000
p = argparse.ArgumentParser()
p.add_argument("--voice", required=True); p.add_argument("--events", required=True)
p.add_argument("--library", required=True); p.add_argument("--out", required=True)
p.add_argument("--ambience", default="amb_room"); p.add_argument("--music", default="music_documentary")
p.add_argument("--seed", type=int, default=7)
p.add_argument("--beat-align", action="store_true", help="shift the music so its strong accents land on reveals/chapters")
A = p.parse_args()
rng = random.Random(A.seed)
os.makedirs(os.path.join(A.out, "stems"), exist_ok=True)
LIB = json.load(open(os.path.join(A.library, "library.json")))
used = []


def load(path):
    tmp = path + ".tmp.wav"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", path, "-ac", "2", "-ar", str(SR), tmp], check=True)
    a, _ = sf.read(tmp, dtype="float32"); os.remove(tmp)
    return a if a.ndim == 2 else np.stack([a, a], 1)


def pick(role, n=None):
    c = [e for e in LIB if e["role"] == role] or [e for e in LIB if e["role"].startswith(role.split("_")[0])]
    if not c:
        return None
    e = c[(n if n is not None else rng.randrange(len(c))) % len(c)]
    used.append(e)
    return load(os.path.join(A.library, e["file"]))


def vary(x, pitch=0.045, gain_db=1.5):
    f = 1 + rng.uniform(-pitch, pitch)
    up, down = int(round(1000 * f)), 1000
    y = resample_poly(x, down, up, axis=0).astype(np.float32)  # faster/slower = pitch shift
    return y * 10 ** (rng.uniform(-gain_db, gain_db) / 20)


def db(x):
    return 10 ** (x / 20)


def hp(x, f):
    return sosfilt(butter(2, f, "high", fs=SR, output="sos"), x, axis=0).astype(np.float32)


def place(track, clip, start):
    s = int(start * SR)
    if s < 0:
        clip = clip[-s:]; s = 0
    e = min(len(track), s + len(clip))
    if e > s:
        track[s:e] += clip[: e - s]


def loop_to(x, n, xfade=2.0):
    """Repeat x with equal-power crossfades until n samples."""
    if len(x) >= n:
        return x[:n].copy()
    xf = min(int(xfade * SR), len(x) // 3)
    fade_in = np.sqrt(np.linspace(0, 1, xf))[:, None]; fade_out = fade_in[::-1]
    out = x.copy()
    while len(out) < n:
        tail = out[-xf:] * fade_out
        head = x[:xf] * fade_in
        out = np.concatenate([out[:-xf], tail + head, x[xf:]])
    return out[:n].astype(np.float32)


ev = json.load(open(A.events))
voice = load(A.voice)
dur = max(ev.get("duration", 0), len(voice) / SR)
N = int(dur * SR) + SR
voice = np.pad(voice, ((0, N - len(voice)), (0, 0)))[:N]
music = np.zeros((N, 2), np.float32); amb = np.zeros((N, 2), np.float32); sfx = np.zeros((N, 2), np.float32)
events = sorted(ev["events"], key=lambda e: e["t"])

# ---- ambience: continuous, two layers, crossfades at place changes (start 0.4 s early) ----
cuts = [(0.0, A.ambience)] + [(e["t"] - 0.4, e["ambience"]) for e in events if e.get("type") == "cut" and e.get("ambience")]
for i, (t0, role) in enumerate(cuts):
    t1 = cuts[i + 1][0] + 2.0 if i + 1 < len(cuts) else dur
    bed = pick(role)
    if bed is None:
        continue
    seg = loop_to(hp(bed, 100), int((t1 - t0) * SR))
    f = int(1.5 * SR); seg[:f] *= np.linspace(0, 1, f)[:, None]; seg[-f:] *= np.linspace(1, 0, f)[:, None]
    place(amb, seg * db(-20), t0)

# ---- music: continuous bed, lifted at chapters, ducked under the voice ----
bed = pick(A.music)
if bed is not None and A.beat_align:
    # onset envelope at 100 Hz; pick the start offset (0–30 s into the track) whose accents best hit the targets
    mono = np.abs(bed).mean(1); hopn = SR // 100
    env = np.array([mono[i:i + hopn].mean() for i in range(0, len(mono) - hopn, hopn)])
    onset = np.clip(np.diff(env, prepend=env[0]), 0, None); onset /= onset.max() + 1e-9
    targets = [e["t"] for e in events if e.get("type") in ("reveal", "chapter")]
    L = len(onset); best, best_sc = 0, -1
    for off in range(0, min(3000, L), 5):
        sc = 0.0
        for t in targets:
            i = int(t * 100 + off) % L
            sc += onset[max(0, i - 10): i + 10].max(initial=0)
        if sc > best_sc:
            best, best_sc = off, sc
    bed = np.roll(bed, -best * hopn, axis=0)
    print(f"beat-align: music starts {best / 100:.2f}s into the track, score {best_sc:.2f}/{len(targets)}")
if bed is not None:
    music = loop_to(bed, N, xfade=3.0) * db(-12)
    f = int(2 * SR); music[:f] *= np.linspace(0, 1, f)[:, None]; music[-int(3 * SR):] *= np.linspace(1, 0, int(3 * SR))[:, None]

# ---- event sounds ----
pre_silence = []
for k, e in enumerate(events):
    t, typ, s = e["t"], e.get("type"), float(e.get("strength", 0.7))
    if typ == "chapter":
        w = pick("whoosh")
        if w is not None:
            w = vary(w); pk = int(np.argmax(np.abs(w).mean(1)))
            place(sfx, w * db(-10 + 4 * s), t - pk / SR)     # peak of the whoosh lands on the transition
    elif typ == "reveal":
        r = pick("riser"); im = pick("impact")
        if r is not None:
            r = r[: int(6 * SR)]; place(sfx, r * db(-14), t - 0.3 - len(r) / SR)
        pre_silence.append((t - 0.3, t))
        if im is not None:
            place(sfx, vary(im, 0.03) * db(-4 + 2 * s), t)
    elif typ in ("number", "doc", "stamp", "photo", "glitch", "hit"):
        role = {"number": "hit_small", "doc": "paper", "stamp": "stamp", "photo": "camera", "glitch": "glitch", "hit": "hit_small"}[typ]
        c = pick(role)
        if c is not None:
            place(sfx, vary(c) * db(-14 + 4 * s), t)

# one shared room: short early-reflection reverb on the SFX bus
ir_len = int(0.35 * SR); ir = np.zeros(ir_len, np.float32); ir[0] = 1
for d, g in ((0.011, .35), (0.019, .28), (0.031, .2), (0.047, .14), (0.071, .09), (0.11, .05)):
    ir[int(d * SR)] += g
sfx = np.stack([fftconvolve(sfx[:, c], ir)[:N] for c in range(2)], 1).astype(np.float32)

# ---- ducking: music −8 dB under voice, −10 dB under impacts; near-silence before reveals ----
win = int(0.3 * SR)
venv = np.convolve(np.abs(voice).mean(1), np.ones(win) / win, mode="same")
vgate = np.clip(venv / (np.percentile(venv[venv > 0], 60) + 1e-9), 0, 1) if venv.any() else np.zeros(N)
senv = np.convolve(np.abs(sfx).mean(1), np.ones(win) / win, mode="same")
sgate = np.clip(senv / (senv.max() * 0.3 + 1e-9), 0, 1)
gain = db(-8 * vgate - 4 * sgate)
for a, b in pre_silence:
    i0, i1 = int(max(0, a - 0.15) * SR), int(b * SR)
    gain[i0:i1] *= db(-14); amb[i0:i1] *= db(-8)
music *= gain[:, None]

stems = {"voice": voice, "music": music, "ambience": amb, "sfx": sfx}
for k, v in stems.items():
    sf.write(os.path.join(A.out, "stems", f"{k}.wav"), v, SR)
mix = voice + music + amb + sfx
mix /= max(1.0, float(np.abs(mix).max()) / 0.95)
raw = os.path.join(A.out, "_mix_raw.wav"); sf.write(raw, mix.astype(np.float32), SR)

# two-pass loudness to −14 LUFS / −1 dBTP
m = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", raw, "-af", "loudnorm=I=-14:TP=-1:LRA=11:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True).stderr
js = json.loads(m[m.rindex("{"): m.rindex("}") + 1])
af = (f"loudnorm=I=-14:TP=-1:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:"
      f"measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
out = os.path.join(A.out, "mix.wav")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", raw, "-af", af, "-ar", str(SR), out], check=True)
os.remove(raw)

# ---- QA without ears ----
qa = {}
r = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
tail = r[r.rfind("Summary:"):]
qa["ebur128"] = " ".join(tail.split())[:300]
r = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", out, "-af", "silencedetect=n=-50dB:d=1.0", "-f", "null", "-"], capture_output=True, text=True).stderr
qa["silences_over_1s"] = r.count("silence_start")
y, _ = sf.read(out, dtype="float32")
qa["clipped_samples"] = int((np.abs(y) > 0.999).sum())
hits = []
for e in events:
    if e.get("type") in ("reveal", "number", "chapter"):
        i = int(e["t"] * SR); seg = np.abs(sfx[max(0, i - SR // 10): i + SR // 5]).mean(1)
        hits.append(round(float(seg.max()) if len(seg) else 0, 3))
qa["event_peaks_min"] = min(hits) if hits else None
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-filter_complex", "showwavespic=s=1800x240:split_channels=0", "-frames:v", "1", os.path.join(A.out, "wave.png")])
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-lavfi", "showspectrumpic=s=1800x400:legend=0", os.path.join(A.out, "spectrum.png")])
json.dump(qa, open(os.path.join(A.out, "sound_qa.json"), "w"), indent=1)
with open(os.path.join(A.out, "credits.txt"), "w") as f:
    seen = set()
    for e in used:
        if e["license"] == "by" and e["id"] not in seen:
            seen.add(e["id"]); f.write(f"\"{e['title']}\" by {e['creator']} — CC BY — {e['source']}\n")
print(json.dumps(qa, ensure_ascii=False))
