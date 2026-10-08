#!/usr/bin/env python3
"""Combine every channel page into one standalone HTML file.

Usage: python3 -I tools/combine.py      (run from lr-map-content/)
Writes dist/lr-map-all.html: one page with a tab per channel and a switch per version. Each piece runs
in its own frame with its own export toolbar, exactly as its standalone dist/ page does. Shared kit files
(fonts, stylesheets, scripts, logos) are stored once and put back into a piece when it is first opened.
"""
import importlib.util, json, os, re

TOOLS = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('gt_build', os.path.join(TOOLS, 'build.py'))
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)
ROOT = B.ROOT
MARK = '\u0001'
OUT = os.path.join(ROOT, 'dist', 'lr-map-all.html')

CHANNELS = [('blog', 'Blog post'), ('reddit', 'Reddit'), ('facebook', 'Facebook'),
            ('instagram', 'Instagram'), ('youtube', 'YouTube')]
VERSIONS = [('opus2', 'Round 2 · Opus'), ('opus', 'Round 1 · Opus'), ('haiku', 'Round 1 · Haiku')]
DESC = {
    'opus2-blog': 'Live-site preview, BlogPost module and share image. Adds a break-even table, a four-relationships table and a reference that stacks on phones.',
    'opus-blog': 'Live-site preview, BlogPost module and share image: six-family table, the library worked example, a grouped reference and frequency shares.',
    'haiku-blog': 'Live-site preview, BlogPost module and share image: source text close to verbatim, a glance table and the full four-column reference.',
    'opus2-reddit': 'Two 1600×1200 images: three answers tested against required and sufficient, and the map of all 20 types. Post text below the images.',
    'opus-reddit': 'Two 1600×1200 images: three answers tested against helpful, required and sufficient, and the map. Post text below the images.',
    'haiku-reddit': 'One 1600×1200 map of the six families. Post text below the image.',
    'opus2-facebook': 'Three 1080×1350 images: the sufficient-or-required chart, the map for the first comment, and the answer reply. Caption below.',
    'opus-facebook': 'Two 1080×1350 images, a caption that ends on a question, and an answer reply.',
    'haiku-facebook': 'One 1080×1350 answer-standards image, the caption and the first comment.',
    'opus2-instagram': 'Fourteen slides and a Story frame: a worked example on every family slide and a review worksheet to close. Caption below.',
    'opus-instagram': 'Thirteen slides, including a four-slide worked example. Caption below.',
    'haiku-instagram': 'Ten slides, each family slide giving every type’s task. Caption below.',
    'opus2-youtube': 'Twenty frames (15:57), two thumbnails, the script, chapters and upload copy.',
    'opus-youtube': 'Twenty-two frames (14:32), two thumbnails, 21 chapters and a teleprompter script.',
    'haiku-youtube': 'Thirteen frames (9:40), one thumbnail, chapters and the script.',
}


class Chunks:
    """Large shared strings, stored once and referenced from each piece as MARK<index>MARK."""
    def __init__(self):
        self.items, self.index = [], {}

    def ref(self, text):
        if text not in self.index:
            self.index[text] = len(self.items)
            self.items.append(text)
        return MARK + str(self.index[text]) + MARK


def css_urls(css, base):
    return re.sub(r'url\((["\']?)(\.\.?/[^)"\']+)\1\)', lambda m: f'url("{B.data_uri(B.kit_path(base, m.group(2)))}")', css)


def linked_css(path):
    return css_urls(open(path, encoding='utf-8').read(), os.path.dirname(path))


def piece(src, chunks):
    """The same output as build.py, with kit files and logo bodies replaced by chunk references."""
    src_dir = os.path.dirname(src)
    html = open(src, encoding='utf-8').read()
    if MARK in html:
        raise SystemExit(f'{src} contains the reserved character U+0001')

    def link(m):
        return '<style>\n' + chunks.ref(linked_css(B.kit_path(src_dir, m.group(1)))) + '\n</style>'

    def script(m):
        js = open(B.kit_path(src_dir, m.group(1)), encoding='utf-8').read().replace('</script', '<\\/script')
        return '<script>\n' + chunks.ref(js) + '\n</script>'

    def svg(m):
        path = B.kit_path(src_dir, m.group(2))
        full = B.inline_svg(path, m.group(1) + m.group(3))
        body = B.inline_svg(path, '')[len('<svg  aria-hidden="true"'):]
        if not full.endswith(body):
            raise SystemExit(f'Unexpected logo markup from build.py for {path}')
        return full[:len(full) - len(body)] + chunks.ref(body)

    html = re.sub(r'<link\b[^>]*?href="((?:\.\./|\./)[^"]+\.css)"[^>]*>', link, html)
    html = re.sub(r'<script\b[^>]*?src="((?:\.\./|\./)[^"]+\.js)"[^>]*>\s*</script>', script, html)
    html = re.sub(r'<img\b([^>]*?)\ssrc="((?:\.\./|\./)[^"]+\.svg)"([^>]*)>', svg, html)
    html = re.sub(r'(<(?:img|image)\b[^>]*?\s(?:src|href)=")((?:\.\./|\./)[^"]+)(")', lambda m: m.group(1) + B.data_uri(B.kit_path(src_dir, m.group(2))) + m.group(3), html)
    html = re.sub(r'<style\b([^>]*)>(.*?)</style>', lambda m: f'<style{m.group(1)}>' + css_urls(m.group(2), src_dir) + '</style>', html, flags=re.S)
    leftovers = re.findall(r'(?:href|src)="(\.\./[^"]+)"', html)
    if leftovers:
        raise SystemExit(f'{src}: not inlined: ' + ', '.join(sorted(set(leftovers))))
    return html


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>LR Map Channel Content</title>
<style id="hub-fonts"></style>
<style>
  :root { --band: #344E73; --ink: #14243B; --body: #28364A; --muted: #5A6B82; --paper: #F3F6FA;
          --wash: #E7EDF5; --line: #C3CEDD; --gold: #E3C06B; }
  html, body { height: 100%; margin: 0; }
  body { display: flex; flex-direction: column; background: var(--wash); color: var(--body);
         font-family: Inter, system-ui, sans-serif; }
  .hub-head { background: var(--band); color: #fff; padding: 14px 16px 0; }
  .hub-row { max-width: 1280px; margin: 0 auto; }
  .hub-title { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; }
  .hub-title svg { height: 30px; width: auto; display: block; }
  .hub-title h1 { margin: 0; font-family: Fraunces, Georgia, serif; font-weight: 550; font-size: 22px;
                  line-height: 1.15; letter-spacing: -0.01em; }
  .hub-eyebrow { margin: 0; font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 500;
                 letter-spacing: 0.06em; text-transform: uppercase; color: var(--gold); }
  .hub-tabs { display: flex; gap: 4px; margin-top: 12px; overflow-x: auto; scrollbar-width: none; }
  .hub-tabs button { flex: 0 0 auto; border: 0; border-radius: 8px 8px 0 0; padding: 10px 16px;
                     background: transparent; color: #DCE4EF; font: 600 15px Inter, system-ui, sans-serif; cursor: pointer; }
  .hub-tabs button:hover { color: #fff; background: rgba(255, 255, 255, 0.08); }
  .hub-tabs button[aria-selected="true"] { background: var(--paper); color: var(--ink); }
  .hub-tabs button:focus-visible, .hub-seg button:focus-visible { outline: 2px solid var(--gold); outline-offset: 2px; }
  .hub-bar { background: var(--paper); border-bottom: 1px solid var(--line); padding: 10px 16px; }
  .hub-bar .hub-row { display: flex; align-items: center; gap: 10px 16px; flex-wrap: wrap; }
  .hub-seg { display: inline-flex; flex-wrap: wrap; border: 1px solid var(--line); border-radius: 8px;
             background: #fff; overflow: hidden; }
  .hub-seg button { border: 0; padding: 8px 12px; background: none; color: var(--body);
                    font: 500 14px Inter, system-ui, sans-serif; cursor: pointer; }
  .hub-seg button + button { border-left: 1px solid var(--line); }
  .hub-seg button[aria-pressed="true"] { background: var(--band); color: #fff; }
  .hub-desc { flex: 1 1 320px; margin: 0; font-size: 14px; line-height: 1.4; color: var(--muted); }
  .hub-stage { position: relative; flex: 1; min-height: 0; }
  @media (max-width: 600px) {
    .hub-head { padding-top: 12px; }
    .hub-title h1 { font-size: 20px; }
    .hub-tabs { flex-wrap: wrap; gap: 6px; margin-top: 10px; padding-bottom: 10px; overflow: visible; }
    .hub-tabs button { border-radius: 8px; padding: 7px 11px; font-size: 14px; }
    .hub-seg { display: grid; grid-template-columns: repeat(3, 1fr); width: 100%; }
    .hub-seg button { padding: 8px 4px; font-size: 13px; line-height: 1.2; }
    .hub-desc { font-size: 13px; }
  }
  .hub-stage iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0;
                      background: var(--wash); visibility: hidden; }
  .hub-stage iframe.on { visibility: visible; }
</style>
</head>
<body>
<header class="hub-head">
  <div class="hub-row hub-title">
    __LOGO__
    <div>
      <p class="hub-eyebrow">LSAT Logical Reasoning · channel content</p>
      <h1>The LR Question Type Map</h1>
    </div>
  </div>
  <div class="hub-row hub-tabs" role="tablist" aria-label="Channel" id="hub-tabs"></div>
</header>
<div class="hub-bar">
  <div class="hub-row">
    <div class="hub-seg" role="group" aria-label="Version" id="hub-seg"></div>
    <p class="hub-desc" id="hub-desc" aria-live="polite"></p>
  </div>
</div>
<main class="hub-stage" id="hub-stage"></main>
<script type="application/json" id="hub-data">__DATA__</script>
<script>
(function () {
  var data = JSON.parse(document.getElementById('hub-data').textContent);
  document.getElementById('hub-fonts').textContent = data.chunks[data.fontChunk];
  var tabs = document.getElementById('hub-tabs'), seg = document.getElementById('hub-seg');
  var desc = document.getElementById('hub-desc'), stage = document.getElementById('hub-stage');
  var frames = {}, state = { channel: data.channels[0][0], version: data.versions[0][0] };

  function label(list, key) { for (var i = 0; i < list.length; i++) if (list[i][0] === key) return list[i][1]; }
  function assemble(html) {
    var parts = html.split('\\u0001');
    for (var i = 1; i < parts.length; i += 2) parts[i] = data.chunks[+parts[i]];
    return parts.join('');
  }
  function button(parent, key, text, attr, pick) {
    var b = document.createElement('button');
    b.type = 'button'; b.textContent = text; b.setAttribute('data-key', key);
    if (attr === 'aria-selected') { b.setAttribute('role', 'tab'); b.setAttribute('aria-controls', 'hub-stage'); }
    b.addEventListener('click', function () { pick(key); });
    parent.appendChild(b);
  }
  function mark(parent, attr, key) {
    Array.prototype.forEach.call(parent.children, function (b) { b.setAttribute(attr, String(b.getAttribute('data-key') === key)); });
  }
  function show() {
    var key = state.version + '-' + state.channel;
    mark(tabs, 'aria-selected', state.channel);
    mark(seg, 'aria-pressed', state.version);
    desc.textContent = data.desc[key];
    if (!frames[key]) {
      var f = document.createElement('iframe');
      f.title = label(data.channels, state.channel) + ', ' + label(data.versions, state.version);
      f.setAttribute('data-key', key);
      f.srcdoc = assemble(data.pieces[key]);
      stage.appendChild(f);
      frames[key] = f;
    }
    Object.keys(frames).forEach(function (k) { frames[k].classList.toggle('on', k === key); });
    try { history.replaceState(null, '', '#' + state.channel + '/' + state.version); } catch (e) {}
    document.title = label(data.channels, state.channel) + ' · ' + label(data.versions, state.version) + ' · LR Map Channel Content';
  }
  data.channels.forEach(function (c) { button(tabs, c[0], c[1], 'aria-selected', function (k) { state.channel = k; show(); }); });
  data.versions.forEach(function (v) { button(seg, v[0], v[1], 'aria-pressed', function (k) { state.version = k; show(); }); });
  function fromHash() {
    var hash = location.hash.replace('#', '').split('/');
    if (label(data.channels, hash[0])) state.channel = hash[0];
    if (label(data.versions, hash[1])) state.version = hash[1];
  }
  window.addEventListener('hashchange', function () { fromHash(); show(); });
  fromHash();
  show();
})();
</script>
</body>
</html>
"""


def main():
    chunks = Chunks()
    font_chunk = int(chunks.ref(linked_css(os.path.join(ROOT, 'kit', 'fonts-social.css'))).strip(MARK))
    pieces = {}
    for v, _ in VERSIONS:
        for c, _ in CHANNELS:
            key = f'{v}-{c}'
            pieces[key] = piece(os.path.join(ROOT, 'src', key + '.html'), chunks)
    data = json.dumps({'channels': CHANNELS, 'versions': VERSIONS, 'desc': DESC, 'fontChunk': font_chunk,
                       'chunks': chunks.items, 'pieces': pieces}, ensure_ascii=False)
    data = data.replace('</', '<\\/').replace('<!--', '\\u003c!--')
    logo = B.inline_svg(os.path.join(ROOT, 'kit', 'logo-white.svg'), 'alt="Germaine Tutoring"')
    html = PAGE.replace('__LOGO__', logo).replace('__DATA__', data)
    if '—' in html:
        raise SystemExit('Em dash found in the combined page')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(html)
    print(f'Built {os.path.relpath(OUT, ROOT)} ({len(html.encode("utf-8")) / 1024:.0f} KB, {len(pieces)} pieces, {len(chunks.items)} shared chunks)')


if __name__ == '__main__':
    main()
