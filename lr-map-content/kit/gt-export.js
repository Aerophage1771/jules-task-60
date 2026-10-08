/* GT export kit.
 * Markup contract:
 *   <section class="gt-set" data-set="Instagram carousel" data-zip="lr-map-instagram"> ...artboards... </section>
 *   <div class="gt-artboard" data-name="slide-01" data-w="1080" data-h="1350"> ... </div>   (data-h="auto" = measured)
 *   <section class="gt-copy" data-label="Caption"><pre>...</pre></section>  (or any element inside instead of <pre>)
 * The kit scales each artboard to fit the screen for preview and exports it at its true size
 * (times the chosen scale) as PNG, JPEG or WebP, one at a time, per set as a ZIP, or everything as a ZIP.
 */
(function () {
  'use strict';
  var state = { format: 'png', scale: 2 };
  var TYPES = { png: 'image/png', jpeg: 'image/jpeg', webp: 'image/webp' };
  var EXT = { png: 'png', jpeg: 'jpg', webp: 'webp' };
  var fontCSS = null;
  var statusEl = null;

  function status(text) { if (statusEl) statusEl.textContent = text || ''; }
  function slug(s) { return String(s || 'image').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); }
  function pageSlug() { return document.body.getAttribute('data-export-name') || slug(document.title); }
  function sizeOf(board) {
    if (board.hasAttribute('data-inline')) return { w: board.offsetWidth, h: board.scrollHeight };
    var w = parseInt(board.getAttribute('data-w'), 10) || board.offsetWidth;
    var hAttr = board.getAttribute('data-h');
    var h = hAttr === 'auto' || !hAttr ? board.scrollHeight : parseInt(hAttr, 10);
    return { w: w, h: h };
  }
  function fileName(board, format) {
    var set = board.closest('.gt-set');
    var base = (set && set.getAttribute('data-zip')) || pageSlug();
    return base + '--' + slug(board.getAttribute('data-name')) + '.' + EXT[format];
  }
  function save(blob, name) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
  }

  function ready() { return document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve(); }

  /* Render one artboard to a Blob at its true size times the scale. */
  function render(board, opts) {
    opts = opts || {};
    var format = opts.format || state.format;
    var scale = opts.scale || state.scale;
    var size = sizeOf(board);
    var lib = window.htmlToImage;
    if (!lib) return Promise.reject(new Error('html-to-image did not load'));
    return ready().then(function () {
      if (fontCSS !== null) return fontCSS;
      return lib.getFontEmbedCSS(board).then(function (css) { fontCSS = css; return css; });
    }).then(function (css) {
      var bg = getComputedStyle(board).backgroundColor;
      if (!bg || bg === 'rgba(0, 0, 0, 0)' || bg === 'transparent') bg = format === 'png' ? null : '#ffffff';
      return lib.toCanvas(board, {
        width: size.w, height: size.h, pixelRatio: scale, fontEmbedCSS: css, backgroundColor: bg || undefined,
        style: { transform: 'none', margin: '0', width: size.w + 'px', height: size.h + 'px' }
      });
    }).then(function (canvas) {
      return new Promise(function (resolve, reject) {
        canvas.toBlob(function (blob) { blob ? resolve(blob) : reject(new Error('Export failed')); }, TYPES[format], format === 'png' ? undefined : 0.95);
      });
    });
  }

  function exportOne(board, format) {
    status('Rendering ' + board.getAttribute('data-name') + '…');
    return render(board, { format: format }).then(function (blob) { save(blob, fileName(board, format)); status('Saved ' + fileName(board, format)); })
      .catch(function (e) { status('Export failed: ' + e.message); throw e; });
  }

  function exportZip(boards, zipName, button) {
    if (!window.JSZip) { status('JSZip did not load'); return Promise.resolve(); }
    if (button) button.disabled = true;
    var zip = new window.JSZip();
    var i = 0;
    function next() {
      if (i >= boards.length) return zip.generateAsync({ type: 'blob' });
      var board = boards[i++];
      status('Rendering ' + i + ' of ' + boards.length + '…');
      return render(board).then(function (blob) { zip.file(fileName(board, state.format), blob); return next(); });
    }
    return next().then(function (blob) { save(blob, zipName + '.zip'); status('Saved ' + zipName + '.zip'); })
      .catch(function (e) { status('Export failed: ' + e.message); })
      .then(function () { if (button) button.disabled = false; });
  }

  function button(label, cls, onClick) {
    var b = document.createElement('button');
    b.type = 'button'; b.textContent = label; if (cls) b.className = cls;
    b.addEventListener('click', onClick);
    return b;
  }

  /* Preview: a fixed-size frame holding the true-size artboard scaled down. Export ignores the frame. */
  var frames = [];
  function layout() {
    frames.forEach(function (f) {
      var size = sizeOf(f.board);
      var set = f.figure.closest('.gt-set-grid') || f.figure.parentElement;
      // A figure inside a page block measures that block, minus any siblings sharing its row.
      var avail = Math.max(200, (set ? set.clientWidth : window.innerWidth) - 2);
      var cap = parseFloat(f.board.getAttribute('data-preview')) || parseFloat((f.figure.closest('.gt-set') || {}).getAttribute && f.figure.closest('.gt-set').getAttribute('data-preview')) || 0;
      var target = cap ? Math.min(cap, avail) : Math.min(avail, size.w);
      var s = Math.min(1, target / size.w);
      f.frame.style.width = Math.round(size.w * s) + 'px';
      f.frame.style.height = Math.round(size.h * s) + 'px';
      f.scaler.style.width = size.w + 'px';
      f.scaler.style.height = size.h + 'px';
      f.scaler.style.transform = 'scale(' + s + ')';
      f.figure.style.width = Math.round(size.w * s) + 'px';
      f.meta.firstChild.textContent = (f.board.getAttribute('data-name') || '') + ' · ' + size.w + '×' + size.h;
    });
  }

  /* An inline board (data-inline) stays in the page at reading size, up to data-w wide, and exports as shown. */
  function wrapInline(board) {
    var w = parseInt(board.getAttribute('data-w'), 10);
    if (w) board.style.maxWidth = w + 'px';
    board.style.width = '100%';
    board.style.marginInline = 'auto';
    var meta = document.createElement('div'); meta.className = 'gt-ab-meta gt-inline-meta';
    var label = document.createElement('span'); label.textContent = (board.getAttribute('data-name') || '') + ' · exports at the width shown';
    var actions = document.createElement('span'); actions.className = 'gt-ab-actions';
    ['png', 'jpeg', 'webp'].forEach(function (fmt) {
      actions.appendChild(button(EXT[fmt].toUpperCase(), '', function (e) {
        var b = e.currentTarget; b.disabled = true;
        exportOne(board, fmt).catch(function () {}).then(function () { b.disabled = false; });
      }));
    });
    meta.appendChild(label); meta.appendChild(actions);
    board.parentNode.insertBefore(meta, board);
  }

  function wrapBoard(board) {
    board.setAttribute('data-gt-wrapped', '');
    if (board.hasAttribute('data-inline')) return wrapInline(board);
    var w = parseInt(board.getAttribute('data-w'), 10);
    var hAttr = board.getAttribute('data-h');
    board.style.width = w + 'px';
    if (hAttr && hAttr !== 'auto') board.style.height = parseInt(hAttr, 10) + 'px';
    board.style.position = board.style.position || 'relative';
    board.style.overflow = 'hidden';
    var figure = document.createElement('figure'); figure.className = 'gt-ab';
    var frame = document.createElement('div'); frame.className = 'gt-ab-frame';
    var scaler = document.createElement('div'); scaler.className = 'gt-ab-scale';
    var meta = document.createElement('figcaption'); meta.className = 'gt-ab-meta';
    meta.appendChild(document.createElement('span'));
    var actions = document.createElement('span'); actions.className = 'gt-ab-actions';
    ['png', 'jpeg', 'webp'].forEach(function (fmt) {
      actions.appendChild(button(EXT[fmt].toUpperCase(), '', function (e) {
        var b = e.currentTarget; b.disabled = true;
        exportOne(board, fmt).catch(function () {}).then(function () { b.disabled = false; });
      }));
    });
    meta.appendChild(actions);
    board.parentNode.insertBefore(figure, board);
    scaler.appendChild(board); frame.appendChild(scaler); figure.appendChild(frame); figure.appendChild(meta);
    frames.push({ board: board, figure: figure, frame: frame, scaler: scaler, meta: meta });
  }

  function setupSets() {
    document.querySelectorAll('.gt-set').forEach(function (set) {
      var boards = Array.prototype.slice.call(set.querySelectorAll('.gt-artboard'));
      // Direct children line up in a grid; artboards nested in the page's own blocks (a storyboard row, say) stay put.
      var grid = document.createElement('div'); grid.className = 'gt-set-grid';
      boards.forEach(function (b) { if (b.parentElement === set) grid.appendChild(b); });
      var head = document.createElement('div'); head.className = 'gt-set-head';
      var h = document.createElement('h2'); h.textContent = set.getAttribute('data-set') || 'Images';
      head.appendChild(h);
      if (boards.length > 1) {
        var zipName = set.getAttribute('data-zip') || pageSlug();
        var zb = button('Download set (' + boards.length + ') as ZIP', 'gt-set-btn', function () { exportZip(boards, zipName, zb); });
        head.appendChild(zb);
      }
      set.insertBefore(grid, set.firstChild);
      set.insertBefore(head, grid);
      if (!grid.children.length) grid.remove();
      boards.forEach(wrapBoard);
    });
    // Artboards outside any set still get controls.
    document.querySelectorAll('.gt-artboard').forEach(function (b) { if (!b.closest('.gt-ab') && !b.hasAttribute('data-gt-wrapped')) wrapBoard(b); });
  }

  function setupCopy() {
    document.querySelectorAll('.gt-copy').forEach(function (block) {
      if (block.querySelector('.gt-copy-box')) return;
      var box = document.createElement('div'); box.className = 'gt-copy-box';
      var head = document.createElement('div'); head.className = 'gt-copy-head';
      var h = document.createElement('h2'); h.textContent = block.getAttribute('data-label') || 'Copy';
      var body = document.createElement('div'); body.className = 'gt-copy-body';
      while (block.firstChild) body.appendChild(block.firstChild);
      var btn = button('Copy text', 'gt-copy-btn', function () {
        var text = block.getAttribute('data-copy-text') || body.innerText.trim();
        var done = function () { btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = 'Copy text'; }, 1400); };
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, function () { fallback(text); done(); });
        else { fallback(text); done(); }
      });
      head.appendChild(h); head.appendChild(btn); box.appendChild(head); box.appendChild(body); block.appendChild(box);
    });
  }
  function fallback(text) {
    var t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select();
    try { document.execCommand('copy'); } catch (e) {}
    t.remove();
  }

  function setupBar() {
    var bar = document.createElement('div'); bar.className = 'gt-kit-bar'; bar.setAttribute('role', 'toolbar'); bar.setAttribute('aria-label', 'Image export');
    var title = document.createElement('strong'); title.textContent = document.body.getAttribute('data-kit-title') || document.title;
    var fmtLabel = document.createElement('label'); fmtLabel.textContent = 'Format';
    var fmt = document.createElement('select');
    [['png', 'PNG'], ['jpeg', 'JPEG'], ['webp', 'WebP']].forEach(function (o) { var op = document.createElement('option'); op.value = o[0]; op.textContent = o[1]; fmt.appendChild(op); });
    fmt.addEventListener('change', function () { state.format = fmt.value; });
    fmtLabel.appendChild(fmt);
    var scLabel = document.createElement('label'); scLabel.textContent = 'Scale';
    var sc = document.createElement('select');
    [['1', '1× (true size)'], ['2', '2× (sharp)'], ['3', '3×']].forEach(function (o) { var op = document.createElement('option'); op.value = o[0]; op.textContent = o[1]; sc.appendChild(op); });
    sc.value = String(state.scale);
    sc.addEventListener('change', function () { state.scale = parseFloat(sc.value); });
    scLabel.appendChild(sc);
    var all = button('Export all images (ZIP)', 'gt-primary', function () {
      exportZip(Array.prototype.slice.call(document.querySelectorAll('.gt-artboard')), pageSlug() + '--all', all);
    });
    statusEl = document.createElement('span'); statusEl.className = 'gt-kit-status'; statusEl.setAttribute('aria-live', 'polite');
    bar.appendChild(title); bar.appendChild(fmtLabel); bar.appendChild(scLabel); bar.appendChild(all); bar.appendChild(statusEl);
    document.body.insertBefore(bar, document.body.firstChild);
  }

  function init() {
    setupBar(); setupSets(); setupCopy(); layout();
    ready().then(layout);
    window.addEventListener('resize', layout);
  }

  window.GTExport = { render: render, exportOne: exportOne, layout: layout, state: state };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
