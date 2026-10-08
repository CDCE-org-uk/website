const { chromium } = require('playwright');
const fs = require('fs');
const [,, S, OUT] = process.argv;
(async () => {
  const b = await chromium.launch({executablePath: '/opt/pw-browsers/chromium'});
  const ctx = await b.newContext({deviceScaleFactor: 1});
  const p = await ctx.newPage();
  const fav = fs.readFileSync(`${S}/logos/favicon.svg`, 'utf8');
  const mark = fs.readFileSync(`${S}/logos/cdce-mark-colour.svg`, 'utf8');
  for (const [name, size, pad, bg] of [['apple-touch-icon',180,22,'#FBF7F0'],['icon-192',192,24,'#FBF7F0'],['icon-512',512,64,'#FBF7F0']]) {
    await p.setViewportSize({width:size,height:size});
    await p.setContent(`<body style="margin:0;background:${bg};display:grid;place-items:center;width:${size}px;height:${size}px">${mark.replace('width="120" height="120"', `width="${size-2*pad}" height="${size-2*pad}"`)}</body>`);
    await p.screenshot({path:`${OUT}/${name}.png`});
  }
  for (const s of [16,32,48]) {
    await p.setViewportSize({width:s,height:s});
    await p.setContent(`<body style="margin:0">${fav.replace('<svg ', `<svg width="${s}" height="${s}" `)}</body>`);
    await p.screenshot({path:`${OUT}/fav-${s}.png`, omitBackground:true});
  }
  // Open Graph image
  const logo = fs.readFileSync(`${S}/logos/cdce-logo-horizontal-colour.svg`, 'utf8');
  const hero = fs.readFileSync(`${S}/hero.svg`, 'utf8');
  await p.setViewportSize({width:1200,height:630});
  await p.setContent(`<style>@font-face{font-family:J;src:url(data:font/woff2;base64,${fs.readFileSync(S+"/fonts/fontsource-variable-plus-jakarta-sans-5.1.1/files/plus-jakarta-sans-latin-wght-normal.woff2").toString("base64")})}</style>
  <body style="margin:0;width:1200px;height:630px;background:#FBF7F0;display:grid;grid-template-columns:1fr 630px;font-family:J">
   <div style="padding:70px 0 60px 70px;display:flex;flex-direction:column;justify-content:space-between">
     <div style="width:380px">${logo.replace(/width="[\d.]+" height="[\d.]+"/, 'width="100%" height="auto"')}</div>
     <div style="font-size:44px;font-weight:800;color:#14304A;line-height:1.12;letter-spacing:-.01em">Space, support and opportunity for <span style="color:#0E6E6B">North East communities</span></div>
     <div style="font-size:24px;font-weight:600;color:#1F4466">cdce.org.uk</div>
   </div>
   <div style="width:630px;height:630px">${hero.replace('<svg ', '<svg width="630" height="630" ')}</div>
   <div style="position:absolute;left:0;right:0;bottom:0;height:10px;background:linear-gradient(90deg,#B23A5F 0 33.3%,#0E6E6B 33.3% 66.6%,#F2A33A 66.6%)"></div>
  </body>`);
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({path:`${OUT}/og-image.png`});
  // Logo PNG exports at 2x
  await ctx.close();
  const ctx2 = await b.newContext({deviceScaleFactor: 4});
  const p2 = await ctx2.newPage();
  for (const f of fs.readdirSync(`${S}/logos`).filter(f => f.endsWith('.svg') && f.startsWith('cdce-'))) {
    const svg = fs.readFileSync(`${S}/logos/${f}`, 'utf8');
    const [, w, h] = svg.match(/width="([\d.]+)" height="([\d.]+)"/);
    await p2.setViewportSize({width:Math.ceil(+w), height:Math.ceil(+h)});
    await p2.setContent(`<body style="margin:0">${svg}</body>`);
    await p2.screenshot({path:`${OUT}/png/${f.replace('.svg','.png')}`, omitBackground:true});
  }
  await b.close();
})();
