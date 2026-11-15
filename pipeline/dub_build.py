#!/usr/bin/env python3
"""COLD WARRANT dub builder. usage:
  dub_build.py bed  <ep_dir>                 -> timing.json + bed.wav (music + FX + nat sound, no English voice)
  dub_build.py voice <ep_dir> <lang> [rate]  -> dub/<lang>/lines/NNN.wav (Edge TTS, one per script line)
  dub_build.py mix  <ep_dir> <lang>          -> dub/<lang>/<ep>_<lang>.mp3 (voice fitted to the English timeline + bed, -14 LUFS)
Timing = same arithmetic as pipeline/build_ep.py (start 1.0 s, + line duration + gap). English line durations from
<ep>/vo/raw_NN.wav (pipeline/tts_ep.py, deterministic Kokoro).
Fitting (owner 2026-11-15 "change the tempo if needed"): our English is fast (x1.15), translations run longer, so each line is
synthesized at a base rate, then sped up with atempo up to MAX_STRETCH; if it still does not fit, it may push into the next pause
(drift) — the drift is absorbed by later pauses. Lines that end > 2.5 s late are reported for re-synthesis/shortening."""
import asyncio, glob, json, os, re, ssl, subprocess, sys, tempfile, importlib.util, urllib.request
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000
MAX_STRETCH = 1.18
BASE_RATE = {"es": 1.10, "pt": 1.10, "hi": 1.08, "fr": 1.10, "it": 1.10, "de": 1.10, "ru": 1.10}
sys.path.insert(0, "/home/claude"); import dub_tts  # noqa: E402

def run(c): subprocess.run(c, check=True)
def load_ep(ep):
    s = importlib.util.spec_from_file_location("e", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(s); s.loader.exec_module(E); return E

def timing(ep):
    E = load_ep(ep); V = []
    for i in range(1, len(E.LINES) + 1):
        info = sf.info(f"{ep}/vo/raw_{i:02d}.wav"); V.append(info.frames / info.samplerate)
    S, t = [], 1.0
    for i, (_, _, o) in enumerate(E.LINES): S.append(t); t += V[i] + o.get("gap", 0.45)
    TOTAL = t; FPS = 30; segs = []; acc = 0.0
    for i, (_, shots, o) in enumerate(E.LINES):
        a = 0.0 if i == 0 else S[i]; b = S[i + 1] if i + 1 < len(E.LINES) else TOTAL
        for j, sh in enumerate(shots):
            d = round((a + (b - a) * (j + 1) / len(shots) - acc) * FPS) / FPS
            n = max(1, int(round(d * FPS))); real = n / FPS
            segs.append(dict(t=acc, d=real, src=str(sh[0]), ss=float(sh[1]))); acc += real
    return E, S, V, TOTAL, segs

def bed(ep):
    E, S, V, TOTAL, segs = timing(ep)
    json.dump(dict(starts=S, vdur=V, total=TOTAL, segs=segs), open(f"{ep}/timing.json", "w"))
    print("TOTAL", round(TOTAL, 2), "video-sum", round(segs[-1]["t"] + segs[-1]["d"], 2))
    LINES = E.LINES; N = int(TOTAL * SR) + SR; t = np.arange(N) / SR; rng = np.random.default_rng(1)
    lp = lambda x, f, o=4: sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)
    bp = lambda x, a, b: sosfilt(butter(2, [a, b], "band", fs=SR, output="sos"), x)
    irl = int(2.6 * SR); ir = rng.standard_normal(irl) * np.exp(-np.arange(irl) / (0.55 * SR)); ir = lp(ir, 5000); ir /= np.sqrt(np.sum(ir**2)) * 3
    # --- same score/FX as pipeline/finish_ep.py ---
    drone = np.zeros(N)
    for f, a in [(55, .5), (82.41, .3), (110, .18), (130.81, .07), (164.81, .05)]:
        lfo = 0.55 + 0.45 * np.sin(2 * np.pi * (0.021 + f / 12000) * t + f)
        drone += a * lfo * np.sin(2 * np.pi * f * t + 0.25 * np.sin(2 * np.pi * 0.07 * t))
    drone += lp(rng.standard_normal(N), 700) * 0.06 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.04 * t))
    hi = sum(np.sin(2 * np.pi * f * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.05 * t + k)) for k, f in enumerate([329.63, 349.23]))
    drone += lp(hi, 1400) * 0.03
    env = np.ones(N) * 0.6; fi = int(2.5 * SR); env[:fi] *= np.linspace(0, 1, fi); eo = int((TOTAL - 5) * SR); env[eo:] *= np.linspace(1, 0, N - eo); drone *= env
    def thump(amp=1.0, f0=52):
        L = int(.5 * SR); tt = np.arange(L) / SR; f = f0 * (1 + 1.6 * np.exp(-tt * 30)); return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)
    chap = [S[i] for i, (_, sh, _) in enumerate(LINES) if any(s[0] == "g:chapter" for s in sh)]
    hunt = chap[3] if len(chap) > 3 else S[0]; crack = chap[5] if len(chap) > 5 else TOTAL
    pulse = np.zeros(N); tt_ = 0.0
    while tt_ < TOTAL - 6:
        fast = (hunt <= tt_ < hunt + 70) or (crack <= tt_ < crack + 40) or tt_ < 25; amp = .55 if fast else .32
        for off, a in [(0, 1), (.22, .55)]:
            i0 = int((tt_ + off) * SR); th = thump(amp * a); pulse[i0:i0 + len(th)] += th[:max(0, min(len(th), N - i0))]
        tt_ += 0.95 if fast else 1.5
    def impact(amp=1.0):
        L = int(4 * SR); tt = np.arange(L) / SR; f = 30 * (1 + 2.6 * np.exp(-tt * 12))
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.6) + lp(rng.standard_normal(L), 3000) * np.exp(-tt * 18) * .6
        x = x + fftconvolve(x, ir)[:L] * .8; return amp * x / np.abs(x).max()
    def riser(d=1.6, amp=.4):
        L = int(d * SR); n_ = rng.standard_normal(L + 4000); out = np.zeros(L); seg = SR // 20
        for k in range(0, L, seg):
            fc = 300 + 5200 * (k / L) ** 2; out[k:k + seg] = bp(n_[k:k + seg + 2000], fc * .7, fc * 1.3)[:len(out[k:k + seg])]
        return amp * out / np.abs(out).max() * (np.arange(L) / L) ** 2
    def whoosh(amp=.35):
        L = int(.7 * SR); tt = np.arange(L) / SR; x = bp(rng.standard_normal(L), 400, 4000) * np.sin(np.pi * tt / tt[-1]) ** 2; return amp * x / np.abs(x).max()
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
    music = drone * .5 + pulse * .45; music = music + fftconvolve(music, ir[:SR])[:N] * .25
    sf.write(f"{ep}/music_raw.wav", (music / np.abs(music).max() * .5).astype(np.float32), SR)
    sf.write(f"{ep}/fx.wav", (fx / max(1e-9, np.abs(fx).max()) * .6).astype(np.float32), SR)
    # --- nat sound: DVIDS clip audio, seeked through the agent proxy ---
    px = os.environ.get("HTTPS_PROXY", ""); urls = {}; mute = [str(x) for x in getattr(E, "META", {}).get("mute_nat", [])]
    os.makedirs(f"{ep}/nat", exist_ok=True); lst = open(f"{ep}/nat/list.txt", "w")
    for k, sg in enumerate(segs):
        out = f"{ep}/nat/{k:03d}.wav"; src = sg["src"]; ok = False
        if not src.startswith(("g:", "img:")) and src not in mute:
            cid = src.split("_")[0]
            try:
                if cid not in urls:
                    d = json.load(urllib.request.urlopen(f"https://api.dvidshub.net/asset?api_key=key-6ae3182ef3840&id=video:{cid}", timeout=30))["results"]
                    fs = sorted([f for f in d["files"] if f.get("height")], key=lambda f: f["height"]); urls[cid] = fs[0]["src"]
                r = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-http_proxy", px, "-ss", str(sg["ss"]), "-i", urls[cid], "-t", f"{sg['d']:.3f}",
                                    "-vn", "-af", "aresample=48000,apad", "-ac", "1", "-t", f"{sg['d']:.3f}", out], timeout=120)
                ok = r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 1000
            except Exception as e:
                print("nat fail", src, e)
        if not ok:
            run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{sg['d']:.3f}", out])
        lst.write(f"file '{k:03d}.wav'\n")
    lst.close()
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{ep}/nat/list.txt",
         "-af", "highpass=f=150,lowpass=f=6000,dynaudnorm=f=200:g=15,volume=0.4", "-ar", str(SR), "-ac", "1", f"{ep}/nat.wav"])
    print("bed parts done")

def voice(ep, lang, rate=None):
    E = load_ep(ep); lines = [l.rstrip("\n") for l in open(f"{ep}/dub/{lang}/script.txt", encoding="utf-8")]
    assert len(lines) == len(E.LINES), (len(lines), len(E.LINES))
    rate = float(rate or BASE_RATE.get(lang, 1.1)); od = f"{ep}/dub/{lang}/lines"; os.makedirs(od, exist_ok=True)
    engine, vname, _ = dub_tts.VOICES[lang]
    todo = [i for i in range(len(lines)) if not os.path.exists(f"{od}/{i+1:03d}.wav")]
    import edge_tts, edge_tts.communicate as ec
    ec._SSL_CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt"); proxy = os.environ.get("HTTPS_PROXY")
    r = f"{int(round((rate - 1) * 100)):+d}%"; sem = asyncio.Semaphore(4); failed = []
    async def one(i):
        text = dub_tts.SPAN.sub(lambda m: m.group(1), lines[i]); mp3 = f"{od}/{i+1:03d}.mp3"
        async with sem:
            for k in range(10):
                try:
                    await edge_tts.Communicate(text, vname, rate=r, proxy=proxy).save(mp3)
                    if os.path.getsize(mp3) > 500: break
                except Exception: pass
                await asyncio.sleep(1 + 1.5 * k)
            else:
                failed.append(i); return
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", mp3, "-af", "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse",
             "-ar", str(SR), "-ac", "1", f"{od}/{i+1:03d}.wav"]); os.remove(mp3)
    async def go(): await asyncio.gather(*[one(i) for i in todo])
    asyncio.run(go())
    for i in failed:  # offline fallback for lines Edge refused
        print("Edge failed on line", i + 1, "-> fallback voice", dub_tts.FALLBACK[lang])
        a, sr = dub_tts.run(lang, lines[i], speed=rate)
        tmp = f"{od}/{i+1:03d}.raw.wav"; sf.write(tmp, a, sr)
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", tmp, "-af", "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse", "-ar", str(SR), "-ac", "1", f"{od}/{i+1:03d}.wav"]); os.remove(tmp)
    json.dump(dict(engine=engine, voice=vname, rate=rate, fallback_lines=[i + 1 for i in failed]), open(f"{ep}/dub/{lang}/voice.json", "w"))
    print(lang, "voiced", len(todo), "lines; fallback:", [i + 1 for i in failed])

def mix(ep, lang):
    T = json.load(open(f"{ep}/timing.json")); S, TOTAL = T["starts"], T["total"]; N = int(TOTAL * SR)
    od = f"{ep}/dub/{lang}"; vo = np.zeros(N + 10 * SR); prev_end = 0.0; report = []
    for i, s in enumerate(S):
        f = f"{od}/lines/{i+1:03d}.wav"; a, sr = sf.read(f, dtype="float32"); a = a if a.ndim == 1 else a.mean(1)
        nxt = S[i + 1] if i + 1 < len(S) else TOTAL - 2.5
        slot = nxt - s - 0.12; L = len(a) / SR; stretch = 1.0
        if L > slot:
            stretch = min(MAX_STRETCH, L / slot)
            tmp = f"{od}/_st.wav"; run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", f, "-af", f"atempo={stretch:.4f}", tmp])
            a, _ = sf.read(tmp, dtype="float32"); a = a if a.ndim == 1 else a.mean(1); L = len(a) / SR
        start = max(s, prev_end + 0.12)
        i0 = int(start * SR); vo[i0:i0 + len(a)] += a; prev_end = start + L
        late = prev_end - (nxt - 0.12)
        report.append(dict(line=i + 1, slot=round(slot, 2), dur=round(L, 2), stretch=round(stretch, 3), delay=round(start - s, 2), late=round(late, 2)))
    vo = vo[:N]
    if prev_end > TOTAL - 0.3: print("WARNING: voice runs past the end by", round(prev_end - TOTAL, 2), "s")
    sf.write(f"{od}/_voice.wav", vo, SR)
    # duck music under the dub voice (as finish_ep does under English)
    music, _ = sf.read(f"{ep}/music_raw.wav", dtype="float32"); music = music[:N]
    win = int(.3 * SR); venv = np.convolve(np.abs(vo), np.ones(win) / win, mode="same")
    duck = 1 - 0.6 * np.clip(venv / (venv.max() * .12 + 1e-9), 0, 1); sf.write(f"{od}/_music.wav", (music * duck[:len(music)]).astype(np.float32), SR)
    out = f"{od}/{os.path.basename(ep.rstrip('/'))}_{lang}.mp3"
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", f"{od}/_voice.wav", "-i", f"{od}/_music.wav", "-i", f"{ep}/fx.wav", "-i", f"{ep}/nat.wav", "-filter_complex",
         "[0:a]aformat=channel_layouts=stereo,asplit[v1][v2];[1:a]aformat=channel_layouts=stereo,volume=0.5[m];[2:a]aformat=channel_layouts=stereo,volume=0.7[f];"
         "[3:a]aformat=channel_layouts=stereo,volume=0.3[n];[n][v2]sidechaincompress=threshold=0.02:ratio=10:attack=20:release=400[nd];"
         "[v1][m][f][nd]amix=inputs=4:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11",
         "-t", f"{TOTAL:.3f}", "-ar", "48000", "-b:a", "192k", out])
    json.dump(report, open(f"{od}/fit_report.json", "w"), indent=0)
    st = [r["stretch"] for r in report]; lates = [r for r in report if r["late"] > 2.5]
    print(lang, out, "dur", subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]).decode().strip(),
          "| stretched lines", sum(x > 1.0 for x in st), "max", max(st), "| max delay", max(r["delay"] for r in report), "| late>2.5s:", [r["line"] for r in lates])

if __name__ == "__main__":
    cmd, ep = sys.argv[1], os.path.abspath(sys.argv[2])
    {"bed": lambda: bed(ep), "voice": lambda: voice(ep, sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None), "mix": lambda: mix(ep, sys.argv[3])}[cmd]()
