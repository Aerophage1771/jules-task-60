/* Exports every artboard in a built page through the page's own export kit, and takes page screenshots.
 * Usage (from lr-map-content/): NODE_PATH=$(npm root -g) node tools/check.js dist/<name>.html
 * Output: .checks/<name>/<artboard>.png (1x, exactly what the Export buttons produce),
 *         .checks/<name>/page-desktop.png and page-phone.png (top of the page only).
 * Fails loudly on console errors, missing fonts or a failed export. */
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const file = path.resolve(process.argv[2]);
  const name = path.basename(file, '.html');
  const out = path.join(path.dirname(path.dirname(file)), '.checks', name);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const errors = [];
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  await page.goto('file://' + file, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const boards = await page.evaluate(() => Array.from(document.querySelectorAll('.gt-artboard')).map((b, i) => ({ i, name: b.getAttribute('data-name') || ('board-' + i), w: b.getAttribute('data-w'), h: b.getAttribute('data-h') })));
  if (!boards.length) errors.push('No .gt-artboard elements found');
  const missingFonts = await page.evaluate(() => Array.from(document.fonts).filter(f => f.status === 'error' && !/Fallback/.test(f.family)).map(f => f.family));
  if (missingFonts.length) errors.push('Fonts failed to load: ' + missingFonts.join(', '));
  for (const b of boards) {
    const res = await page.evaluate(async (i) => {
      const board = document.querySelectorAll('.gt-artboard')[i];
      try {
        const blob = await window.GTExport.render(board, { format: 'png', scale: 1 });
        const buf = new Uint8Array(await blob.arrayBuffer());
        let s = ''; for (let k = 0; k < buf.length; k += 0x8000) s += String.fromCharCode.apply(null, buf.subarray(k, k + 0x8000));
        return { ok: true, data: btoa(s) };
      } catch (e) { return { ok: false, error: String(e && e.message || e) }; }
    }, b.i);
    if (!res.ok) { errors.push(`Export failed for ${b.name}: ${res.error}`); continue; }
    const fn = path.join(out, String(b.i + 1).padStart(2, '0') + '-' + b.name.replace(/[^a-z0-9-]+/gi, '-') + '.png');
    fs.writeFileSync(fn, Buffer.from(res.data, 'base64'));
    console.log(`exported ${b.name} (${b.w}x${b.h || 'auto'}) -> ${path.relative(process.cwd(), fn)}`);
  }
  await page.screenshot({ path: path.join(out, 'page-desktop.png') });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(out, 'page-phone.png') });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  if (overflow) errors.push('Horizontal scroll at 390px phone width');
  await browser.close();
  if (errors.length) { console.error('PROBLEMS:\n- ' + errors.join('\n- ')); process.exit(1); }
  console.log('OK: ' + boards.length + ' artboards exported, no console errors.');
})();
