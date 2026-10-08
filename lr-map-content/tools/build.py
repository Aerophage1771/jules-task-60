#!/usr/bin/env python3
"""Build a standalone HTML file from an authored page.

Usage: python3 -I tools/build.py src/<name>.html      (run from lr-map-content/)
Writes dist/<name>.html with every ../kit/ stylesheet, script and image inlined, so the file
works offline, opened straight from disk, and exports images with the correct fonts.
"""
import base64, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIME = {'.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.woff2': 'font/woff2'}


def kit_path(src_dir, ref):
    path = os.path.normpath(os.path.join(src_dir, ref))
    if not path.startswith(ROOT + os.sep):
        raise SystemExit(f'Refusing to inline a file outside lr-map-content: {ref}')
    if not os.path.isfile(path):
        raise SystemExit(f'Missing file referenced by the page: {ref}')
    return path


def data_uri(path):
    ext = os.path.splitext(path)[1].lower()
    with open(path, 'rb') as f:
        return f'data:{MIME.get(ext, "application/octet-stream")};base64,' + base64.b64encode(f.read()).decode()


def inline_svg(path, attrs):
    """An <img> of a kit SVG becomes the SVG itself: html-to-image drops SVG <img> sources on export."""
    svg = open(path, encoding='utf-8').read().strip()
    keep = ' '.join(re.findall(r'\s((?:class|style|id|width|height)="[^"]*")', ' ' + attrs))
    alt = re.search(r'\salt="([^"]*)"', ' ' + attrs)
    label = f' role="img" aria-label="{alt.group(1)}"' if alt and alt.group(1) else ' aria-hidden="true"'
    svg = re.sub(r'\s(?:role|aria-label)="[^"]*"', '', svg, count=2)
    svg = re.sub(r'<title>.*?</title>', '', svg, count=1, flags=re.S)
    return re.sub(r'^<svg\b', '<svg ' + keep + label, svg, count=1)


def build(src):
    src = os.path.abspath(src)
    src_dir = os.path.dirname(src)
    html = open(src, encoding='utf-8').read()

    def css_urls(css, base):
        return re.sub(r'url\((["\']?)(\.\.?/[^)"\']+)\1\)', lambda m: f'url("{data_uri(kit_path(base, m.group(2)))}")', css)

    def link(m):
        path = kit_path(src_dir, m.group(1))
        css = css_urls(open(path, encoding='utf-8').read(), os.path.dirname(path))
        return '<style>\n' + css + '\n</style>'

    def script(m):
        js = open(kit_path(src_dir, m.group(1)), encoding='utf-8').read().replace('</script', '<\\/script')
        return '<script>\n' + js + '\n</script>'

    html = re.sub(r'<link\b[^>]*?href="((?:\.\./|\./)[^"]+\.css)"[^>]*>', link, html)
    html = re.sub(r'<script\b[^>]*?src="((?:\.\./|\./)[^"]+\.js)"[^>]*>\s*</script>', script, html)
    html = re.sub(r'<img\b([^>]*?)\ssrc="((?:\.\./|\./)[^"]+\.svg)"([^>]*)>', lambda m: inline_svg(kit_path(src_dir, m.group(2)), m.group(1) + m.group(3)), html)
    html = re.sub(r'(<(?:img|image)\b[^>]*?\s(?:src|href)=")((?:\.\./|\./)[^"]+)(")', lambda m: m.group(1) + data_uri(kit_path(src_dir, m.group(2))) + m.group(3), html)
    html = re.sub(r'<style\b([^>]*)>(.*?)</style>', lambda m: f'<style{m.group(1)}>' + css_urls(m.group(2), src_dir) + '</style>', html, flags=re.S)

    leftovers = re.findall(r'(?:href|src)="(\.\./[^"]+)"', html)
    if leftovers:
        raise SystemExit('Not inlined (only ../kit/ assets are supported): ' + ', '.join(sorted(set(leftovers))))
    out = os.path.join(ROOT, 'dist', os.path.basename(src))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
    print(f'Built {os.path.relpath(out, ROOT)} ({len(html) / 1024:.0f} KB)')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for arg in sys.argv[1:]:
        build(arg)
