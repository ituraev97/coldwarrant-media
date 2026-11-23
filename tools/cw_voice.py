#!/usr/bin/env python3
"""COLD WARRANT narration in Chatterbox (natural male voice, owner decision 2026-11-23) via the owner's server.
Wraps tools/tts_client.py for episode.py.

  python3 tools/cw_voice.py request RUN EPISODE_DIR --creds /tmp/drive_creds.json [--hint "names"]
      Orders every LINES text as vo/raw_NN.wav (1-based, exactly what pipeline/tts_ep.py writes). Per-line pace follows opts
      "speed" (relative to the 1.04 default) on top of BASE_TEMPO. Takes ~3–6 h on the server, so the NEXT run builds it.
  python3 tools/cw_voice.py status RUN --creds ...
  python3 tools/cw_voice.py fetch RUN EPISODE_DIR --creds ...
      Writes EPISODE_DIR/vo/raw_NN.wav. pipeline/tts_ep.py then skips every existing file (Kokoro only fills gaps —
      any gap means mixed voices: never change LINES text after `request`).
"""
import importlib.util, json, os, subprocess, sys, argparse, tempfile

VOICE = "cw"          # reference voice on the server (owner-approved sample)
BASE_TEMPO = 1.08     # Chatterbox is slower than Kokoro x1.15; 1.08 keeps it brisk without artefacts
HERE = os.path.dirname(os.path.abspath(__file__))

def lines(ep):
    spec = importlib.util.spec_from_file_location("episode", os.path.join(ep, "episode.py"))
    E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
    return E.LINES

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["request", "status", "fetch"]); ap.add_argument("run"); ap.add_argument("ep", nargs="?")
    ap.add_argument("--creds", default="/tmp/drive_creds.json"); ap.add_argument("--hint", default="")
    a = ap.parse_args()
    client = [sys.executable, os.path.join(HERE, "tts_client.py")]
    if a.cmd == "request":
        L = lines(os.path.abspath(a.ep))
        spec = {"vo": {"lines": [t for t, _, _ in L],
                       "names": [f"raw_{i:02d}.wav" for i in range(1, len(L) + 1)],
                       "tempos": [round(BASE_TEMPO * float(o.get("speed", 1.04)) / 1.04, 3) for _, _, o in L],
                       "voice": VOICE, "polish": False}}   # build_ep.py applies the channel EQ + loudnorm itself
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False); json.dump(spec, f); f.close()
        sys.exit(subprocess.call(client + ["request-spec", a.run, f.name, "--creds", a.creds, "--hint", a.hint]))
    if a.cmd == "status":
        sys.exit(subprocess.call(client + ["status", a.run, "--creds", a.creds]))
    sys.exit(subprocess.call(client + ["fetch", a.run, os.path.abspath(a.ep), "--creds", a.creds]))

if __name__ == "__main__":
    main()
