#!/usr/bin/env bash
# usage: encode.sh <episode_dir> <out.mp4> [max_MB=95]
# Burns subs.ass, fades, muxes mix.wav, 2-pass H.265 sized under the GitHub 100 MB limit.
set -euo pipefail
EP="$1"; OUT="$2"; MAXMB="${3:-95}"
cd "$EP"
D=$(python3 -c "import json;print(json.load(open('timing.json'))['total'])")
FO=$(python3 -c "print($D-0.8)")
ABR=128
VBR=$(python3 -c "print(int(($MAXMB*8*1024*0.97)/$D - $ABR))")
echo "duration $D s -> video ${VBR}k"
VF="fade=t=in:st=0:d=0.6,fade=t=out:st=$FO:d=0.8,ass=subs.ass"
ffmpeg -nostdin -v error -y -i video_raw.mp4 -vf "$VF" -c:v libx265 -preset fast -b:v ${VBR}k -x265-params pass=1:log-level=error -an -f null /dev/null
ffmpeg -nostdin -v error -y -i video_raw.mp4 -i mix.wav -vf "$VF" -c:v libx265 -preset fast -b:v ${VBR}k -x265-params pass=2:log-level=error \
  -tag:v hvc1 -pix_fmt yuv420p -c:a aac -b:a ${ABR}k -ar 48000 -t "$D" -movflags +faststart "$OUT"
rm -f x265_2pass.log*
ls -la "$OUT"
