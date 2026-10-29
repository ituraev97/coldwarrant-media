#!/usr/bin/env python3
"""Narration with Kokoro. usage: tts_ep.py <episode_dir> [voice] [lang]
Writes <ep>/vo/raw_NN.wav for each line in episode.LINES (skips existing)."""
import sys, os, importlib.util, soundfile as sf
ep = os.path.abspath(sys.argv[1]); voice = sys.argv[2] if len(sys.argv) > 2 else "am_michael"
lang = sys.argv[3] if len(sys.argv) > 3 else "en-us"
spec = importlib.util.spec_from_file_location("episode", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
from kokoro_onnx import Kokoro
M = os.environ.get("KOKORO_DIR", "/home/claude/tts")
k = Kokoro(f"{M}/kokoro-v1.0.onnx", f"{M}/voices-v1.0.bin")
os.makedirs(f"{ep}/vo", exist_ok=True)
tot = 0
for i, (t, shots, o) in enumerate(E.LINES, 1):
    f = f"{ep}/vo/raw_{i:02d}.wav"
    if not os.path.exists(f):
        a, sr = k.create(t, voice=voice, speed=float(os.environ.get("TTS_SPEED", "1.06")), lang=lang); sf.write(f, a, sr)  # RULE: speed 1.06 (ep.001 used 0.94 — too slow)
    a, sr = sf.read(f); tot += len(a) / sr
print("speech seconds:", round(tot, 1))
