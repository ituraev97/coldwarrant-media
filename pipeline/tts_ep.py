#!/usr/bin/env python3
"""Narration with Kokoro. usage: tts_ep.py <episode_dir> [voice] [lang]
Writes <ep>/vo/raw_NN.wav for each line in episode.LINES (skips existing)."""
import sys, os, importlib.util, soundfile as sf
ep = os.path.abspath(sys.argv[1]); voice = sys.argv[2] if len(sys.argv) > 2 else "bm_george:0.5+am_onyx:0.5"  # RULE: channel voice since 2026-11-14 (owner chose sample D)
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
SCALE = float(os.environ.get("TTS_SCALE", "1.15"))  # RULE: owner 2026-11-14 "faster": real speed = per-line speed x 1.15
tot = 0
for i, (t, shots, o) in enumerate(E.LINES, 1):
    f = f"{ep}/vo/raw_{i:02d}.wav"
    if not os.path.exists(f):
        a, sr = k.create(t, voice=VOICE, speed=float(o.get("speed", 1.04)) * SCALE, lang=lang); sf.write(f, a, sr)  # RULE: per-line o["speed"] 0.94–1.10 (relative) for rhythm, default 1.04
    a, sr = sf.read(f); tot += len(a) / sr
print("speech seconds:", round(tot, 1))
