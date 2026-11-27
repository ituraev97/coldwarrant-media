#!/usr/bin/env python3
"""Narration with Kokoro. usage: tts_ep.py <episode_dir> [voice] [lang]
Writes <ep>/vo/raw_NN.wav for each line in episode.LINES (skips existing)."""
import sys, os, importlib.util, soundfile as sf
ep = os.path.abspath(sys.argv[1]); voice = sys.argv[2] if len(sys.argv) > 2 else "bm_fable:0.4+am_michael:0.3+bm_george:0.3"  # RULE: channel voice since 2026-11-27 (owner chose sample C, "livelier"); before: bm_george:0.5+am_onyx:0.5
lang = sys.argv[3] if len(sys.argv) > 3 else "en-us"
spec = importlib.util.spec_from_file_location("episode", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
from kokoro_onnx import Kokoro
M = os.environ.get("KOKORO_DIR", "/home/claude/tts")
k = Kokoro(f"{M}/kokoro-v1.0.onnx", f"{M}/voices-v1.0.bin")
os.makedirs(f"{ep}/vo", exist_ok=True)
def style(spec):  # "a:0.5+b:0.5" -> blended voice style
    if "+" not in spec: return spec
    return sum(k.get_voice_style(n) * float(w) for n, w in (p.split(":") for p in spec.split("+")))
VOICE = style(voice)
import re, random, numpy as np
# RULE (owner 2026-11-27, livelier Kokoro): per-sentence synthesis, short sentences slower + longer pause, long ones quicker, +-2% jitter
def sents(t): return [x.strip() for x in re.split(r'(?<=[.?!])\s+', t) if x.strip()]
def render(t, rel):
    parts = []; sr = 24000
    for sent in sents(t):
        n = len(sent.split())
        sp = (0.98 if n <= 5 else 1.02 if n <= 14 else 1.08) * 1.05 * random.uniform(0.98, 1.02) * rel
        a, sr = k.create(sent, voice=VOICE, speed=sp, lang=lang); parts.append(a)
        gap = {'.': 0.42, '?': 0.55, '!': 0.45}.get(sent[-1], 0.35) + (0.18 if n <= 5 else 0)
        parts.append(np.zeros(int(sr * gap), dtype=np.float32))
    return np.concatenate(parts[:-1]), sr  # no trailing gap: build_ep adds o["gap"] between lines
tot = 0
for i, (t, shots, o) in enumerate(E.LINES, 1):
    f = f"{ep}/vo/raw_{i:02d}.wav"
    if not os.path.exists(f):
        random.seed(i); a, sr = render(t, float(o.get("speed", 1.0))); sf.write(f, a, sr)
    a, sr = sf.read(f); tot += len(a) / sr
print("speech seconds:", round(tot, 1))
