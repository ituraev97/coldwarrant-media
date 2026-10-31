// Thumbnail generator (COLD WARRANT style). usage: node thumb.mjs <thumb.json> <out_dir>
// thumb.json: {"image": "/abs/frame.jpg", "pos": "55% 18%", "zoom": 118,
//   "A": {"big": "MS-<r>13</r>", "tag": "BORN IN L.A."},          // main: huge 1–2 words + amber tag
//   "C": {"kicker": "FROM L.A. KIDS", "big": "TO <r>TERROR</r><br>LIST"}}  // alt for Test & Compare
// Rules: max ~5 words, nothing in bottom-right (duration badge), no gore, no weapons pointed at camera.
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const NM = path.resolve("node_modules"); const cfg = JSON.parse(fs.readFileSync(process.argv[2])); const out = process.argv[3];
fs.mkdirSync(out, { recursive: true });
const r = (s) => s.replace(/<r>/g, '<span style="color:#D3212D">').replace(/<\/r>/g, "</span>");
const CSS = `@font-face{font-family:Anton;src:url(file://${NM}/@fontsource/anton/files/anton-latin-400-normal.woff2)}
*{margin:0;padding:0;box-sizing:border-box}body{background:#000}
.t{position:relative;width:1280px;height:720px;overflow:hidden;background:#0A0A0B;color:#ECE7DC}
.ph{position:absolute;right:-120px;top:-40px;width:1000px;height:800px;background-image:url(data:image/jpeg;base64,${fs.readFileSync(cfg.image).toString("base64")});background-repeat:no-repeat;background-position:${cfg.pos || "50% 30%"};background-size:${cfg.zoom || 118}%}
.anton{font-family:Anton;line-height:.86}.sh{text-shadow:0 6px 0 rgba(0,0,0,.55),0 0 40px rgba(0,0,0,.6)}
.tag{display:inline-block;font-family:Anton;color:#0A0A0B;background:#E8A33D;padding:8px 20px 4px;transform:rotate(-2deg)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 180px rgba(0,0,0,.75)}
.logo{position:absolute;left:44px;bottom:36px;display:flex;gap:10px;font-family:Anton;font-size:38px;align-items:center}.logo i{font-style:normal;background:#D3212D;padding:2px 10px 0}`;
const grad = (p) => `<div style="position:absolute;inset:0;background:linear-gradient(90deg,#0A0A0B 0%,#0A0A0B ${p}%,rgba(10,10,11,.65) ${p + 13}%,rgba(10,10,11,0) ${p + 27}%)"></div><div class="vig"></div>`;
const html = {
  A: (o) => `<div class="t"><div class="ph"></div>${grad(31)}<div style="position:absolute;left:40px;top:58px">
     <div class="anton sh" style="font-size:${o.size || 286}px;letter-spacing:-4px">${r(o.big)}</div>
     <div class="tag" style="font-size:${o.tsize || 100}px;margin-top:22px">${o.tag}</div></div>
     <div class="logo"><span>COLD</span><i>WARRANT</i></div></div>`,
  C: (o) => `<div class="t"><div class="ph"></div>${grad(36)}<div style="position:absolute;left:40px;top:54px;width:600px">
     <div class="anton" style="font-size:${o.ksize || 84}px;color:#E8A33D">${o.kicker}</div>
     <div class="anton sh" style="font-size:${o.size || 176}px;margin-top:8px">${r(o.big)}</div></div>
     <div class="logo"><span>COLD</span><i>WARRANT</i></div></div>`,
};
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
for (const k of ["A", "C"]) {
  if (!cfg[k]) continue;
  await pg.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${html[k](cfg[k])}</body></html>`);
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(800);
  await pg.screenshot({ path: path.join(out, `thumb_${k}.jpg`), type: "jpeg", quality: 92 });
  console.log("thumb", k);
}
await b.close();
