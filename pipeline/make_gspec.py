#!/usr/bin/env python3
"""usage: make_gspec.py <episode_dir>  -> writes <ep>/gspec.json for graphics.mjs"""
import json, hashlib, importlib.util, os, sys
ep = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("episode", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
out = {}
for t, shots, o in E.LINES:
    for s in shots:
        if s[0].startswith("g:"):
            name, opts = s[0][2:], s[2]
            key = name + "_" + hashlib.md5(json.dumps(opts, sort_keys=True).encode()).hexdigest()[:6]
            out[key] = dict(key=key, name=name, opts=opts, intro=2.4)
json.dump(list(out.values()), open(os.path.join(ep, "gspec.json"), "w"), indent=1)
print(len(out), "graphics")
