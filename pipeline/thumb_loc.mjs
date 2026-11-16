// Localized thumbnails for dub languages: re-texts a published English thumb_A (news layout) — usage: node thumb_loc.mjs loc.json /abs/thumb_A.jpg out_dir
// needs: npm i @fontsource/teko (Devanagari) in /home/claude/work/loc or adjust TK; Cyrillic via Oswald, Latin via Anton. Example spec: episodes/016-tony-montana/dub/thumb_loc.json
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const require = createRequire("/home/claude/coldwarrant-media/pipeline/x.js"); const { chromium } = require("playwright");
const NM="/home/claude/coldwarrant-media/pipeline/node_modules/@fontsource", TK="/home/claude/work/loc/node_modules/@fontsource/teko/files";
const L = JSON.parse(fs.readFileSync(process.argv[2],"utf8"));
const css = `@font-face{font-family:Anton;src:url(file://${NM}/anton/files/anton-latin-400-normal.woff2)}
@font-face{font-family:Anton;src:url(file://${NM}/anton/files/anton-latin-ext-400-normal.woff2);unicode-range:U+0100-024F}
@font-face{font-family:Osw;font-weight:700;src:url(file://${NM}/oswald/files/oswald-cyrillic-700-normal.woff2);unicode-range:U+0400-04FF}
@font-face{font-family:Osw;font-weight:700;src:url(file://${NM}/oswald/files/oswald-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F}
@font-face{font-family:Teko;font-weight:600;src:url(file://${TK}/teko-devanagari-600-normal.woff2);unicode-range:U+0900-097F,U+200C-200D,U+25CC}
@font-face{font-family:Teko;font-weight:600;src:url(file://${TK}/teko-latin-600-normal.woff2);unicode-range:U+0000-00FF,U+2000-206F}
*{margin:0;padding:0;box-sizing:border-box}body{width:1280px;height:720px;overflow:hidden;background:#000}
.t{position:relative;width:1280px;height:720px;background:url(file://${process.argv[3]})}
.band{position:absolute;left:0;right:0;top:390px;bottom:0;background:linear-gradient(180deg,rgba(8,8,9,0) 0,rgba(8,8,9,.97) 62px,#080809 75px)}
.tag{position:absolute;left:0;top:18px;height:110px;min-width:296px;display:flex;align-items:center;padding:6px 26px 0 22px;background:#FF2A2A;color:#fff;border:5px solid #000;border-left:0;font-size:62px}
.lab{position:absolute;right:166px;top:208px;min-width:342px;height:54px;display:flex;align-items:center;justify-content:center;padding:0 14px;background:#000;color:#fff;font-size:26px;letter-spacing:1px}
.txt{position:absolute;left:20px;right:20px;bottom:28px;text-align:center;line-height:1.02;text-transform:uppercase}
.txt div{-webkit-text-stroke:8px #000;paint-order:stroke fill;text-shadow:0 6px 0 #000}`;
const b = await chromium.launch(); const pg = await b.newPage({ viewport:{width:1280,height:720} });
for (const [k,o] of Object.entries(L)) {
  const f = o.font || "Anton", tw = o.font==="Teko" ? "font-weight:600;" : o.font==="Osw" ? "font-weight:700;" : "";
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="t"><div class="band"></div>
   <div class="tag" style="font-family:${f};${tw}${o.tsize?`font-size:${o.tsize}px;`:""}">${o.tag}</div><div class="lab" style="font-family:${f};${tw}">${o.lab}</div>
   <div class="txt" style="font-family:${f};${tw}"><div style="font-size:${o.s1||104}px;color:#fff">${o.l1}</div><div style="font-size:${o.s2||118}px;color:#FFD400">${o.l2}</div></div></div></body></html>`;
  const tmp = path.resolve(`_${k}.html`); fs.writeFileSync(tmp, html); await pg.goto("file://"+tmp);
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(300);
  await pg.screenshot({ path:path.join(process.argv[4], `thumb_${k}.jpg`), type:"jpeg", quality:93 }); fs.unlinkSync(tmp); console.log(k);
}
await b.close();
