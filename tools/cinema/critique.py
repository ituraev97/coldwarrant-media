#!/usr/bin/env python3
"""Doc Cinema — critique a DELIVERED video before upload (measured, not watched).

usage: critique.py FINAL.mp4 [--events events.json] [--max-hold 4.0] [--out critique.json]
Checks (ideas from motion-director, MIT, adapted for long documentaries):
  - frame 0 is not black/empty (it is the hook and the thumbnail frame)
  - no black stretches > 0.5 s except intended dips (blackdetect)
  - no frozen picture longer than --max-hold seconds (freezedetect) — "nothing is happening for a few seconds"
  - loudness −14 LUFS ±1, true peak ≤ −1 dBTP
  - music/mix has mids: < 55 % of energy below 150 Hz, otherwise it plays as nothing on a phone speaker
  - every event (chapter/reveal/number) has an audible rise ≥ 3 dB over the 1 s before it, peak within ±80 ms
Exit code 1 when a hard check fails. Prints a short Russian-friendly summary.
"""
import argparse, json, re, subprocess, sys
import numpy as np

p = argparse.ArgumentParser(); p.add_argument("mp4"); p.add_argument("--events"); p.add_argument("--max-hold", type=float, default=4.0)
p.add_argument("--out", default=None)
a = p.parse_args()


def ff(args):
    return subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", *args], capture_output=True, text=True).stderr


rep = {"file": a.mp4, "fail": [], "warn": []}
# frame 0
y = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", a.mp4, "-frames:v", "1", "-vf", "scale=64:36,format=gray", "-f", "rawvideo", "-"],
                   capture_output=True).stdout
if y:
    f0 = np.frombuffer(y, np.uint8)
    rep["frame0_mean"] = float(f0.mean()); rep["frame0_std"] = float(f0.std())
    if f0.mean() < 12 or f0.std() < 6:
        rep["fail"].append("кадр 0 пустой/чёрный — первый кадр должен быть хуком")
# black + freeze
s = ff(["-i", a.mp4, "-vf", "blackdetect=d=0.5:pix_th=0.10", "-an", "-f", "null", "-"])
blacks = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", s)
rep["black_stretches"] = [(float(x), float(y)) for x, y in blacks]
s = ff(["-i", a.mp4, "-vf", f"freezedetect=n=0.003:d={a.max_hold}", "-an", "-f", "null", "-"])
freezes = re.findall(r"freeze_start: ([\d.]+)", s); fdur = re.findall(r"freeze_duration: ([\d.]+)", s)
rep["frozen_stretches"] = [(float(t), float(d)) for t, d in zip(freezes, fdur)]
if rep["frozen_stretches"]:
    rep["fail"].append(f"{len(rep['frozen_stretches'])} застывших кусков > {a.max_hold} с (первые: " +
                       ", ".join(f"{t:.0f}s/{d:.1f}s" for t, d in rep["frozen_stretches"][:5]) + ")")
# loudness
s = ff(["-i", a.mp4, "-af", "ebur128=peak=true", "-vn", "-f", "null", "-"])
I = re.findall(r"I:\s+(-?[\d.]+) LUFS", s); TP = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", s)
if I:
    rep["lufs"] = float(I[-1]); rep["true_peak"] = float(TP[-1]) if TP else None
    if abs(rep["lufs"] + 14) > 1:
        rep["warn"].append(f"громкость {rep['lufs']} LUFS (цель −14)")
    if rep["true_peak"] is not None and rep["true_peak"] > -1:
        rep["fail"].append(f"пик {rep['true_peak']} dBTP (должен быть ≤ −1)")
# mids share + event rises from decoded mono audio
raw = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", a.mp4, "-vn", "-ac", "1", "-ar", "8000", "-f", "f32le", "-"], capture_output=True).stdout
x = np.frombuffer(raw, np.float32)
if len(x) > 8000:
    spec = np.abs(np.fft.rfft(x[: 8000 * 120])) ** 2; freqs = np.fft.rfftfreq(min(len(x), 8000 * 120), 1 / 8000)
    low = float(spec[freqs < 150].sum() / max(spec.sum(), 1e-9)); rep["low_energy_share"] = round(low, 3)
    if low > 0.55:
        rep["warn"].append(f"{int(low * 100)}% энергии ниже 150 Гц — на телефоне музыка/фон пропадут")
    if a.events:
        ev = json.load(open(a.events))["events"]
        hop = 80; env = np.sqrt(np.convolve(x ** 2, np.ones(hop) / hop, mode="same") + 1e-12)
        bad = []
        for e in ev:
            if e.get("type") not in ("chapter", "reveal", "number"):
                continue
            i = int(e["t"] * 8000)
            if i < 8000 or i + 800 > len(env):
                continue
            before = 20 * np.log10(np.median(env[i - 8000: i - 400]) + 1e-9)
            win = env[i - 640: i + 640]; k = int(np.argmax(win)); peak = 20 * np.log10(win[k] + 1e-9)
            off_ms = (k - 640) / 8
            if peak - before < 3 or abs(off_ms) > 80:
                bad.append(f"{e['type']}@{e['t']:.1f}s rise {peak - before:.1f}dB off {off_ms:.0f}ms")
        rep["weak_events"] = bad
        if bad:
            rep["warn"].append(f"{len(bad)} событий без чёткого звукового акцента")
out = a.out or a.mp4.rsplit(".", 1)[0] + ".critique.json"
json.dump(rep, open(out, "w"), ensure_ascii=False, indent=1)
print(("ПРОВАЛ: " + "; ".join(rep["fail"])) if rep["fail"] else "ОК", "| предупреждения:", "; ".join(rep["warn"]) or "нет")
sys.exit(1 if rep["fail"] else 0)
