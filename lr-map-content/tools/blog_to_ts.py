#!/usr/bin/env python3
"""Turn a blog preview page into a site post module.

Usage: python3 -I tools/blog_to_ts.py src/<model>-blog.html      (run from lr-map-content/)
Reads <script type="application/json" id="post-meta"> and the HTML between
<!-- POST-CONTENT:START --> and <!-- POST-CONTENT:END -->, then writes copy/<model>-blog.ts:
a BlogPost module for apps/germainetutoring-website/client/src/data/posts/ in Business_Planner.
"""
import json, math, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ['slug', 'title', 'metaTitle', 'date', 'snippet', 'metaDescription', 'tags', 'author', 'readTime', 'featured_image', 'social_image', 'social_image_alt']


def main(src):
    html = open(src, encoding='utf-8').read()
    meta_m = re.search(r'<script type="application/json" id="post-meta">(.*?)</script>', html, re.S)
    body_m = re.search(r'<!-- POST-CONTENT:START -->(.*?)<!-- POST-CONTENT:END -->', html, re.S)
    if not meta_m or not body_m:
        raise SystemExit('Need <script type="application/json" id="post-meta"> and POST-CONTENT:START/END markers.')
    meta = json.loads(meta_m.group(1))
    body = body_m.group(1).strip('\n')
    words = len(re.sub(r'<[^>]+>', ' ', body).split())
    meta.setdefault('readTime', max(1, math.ceil(words / 230)))
    meta.setdefault('author', 'Germaine Washington')
    for key in ['slug', 'title', 'date', 'snippet', 'tags']:
        if key not in meta:
            raise SystemExit(f'post-meta is missing {key}')
    if '—' in body or any('—' in str(v) for v in meta.values()):
        raise SystemExit('Em dash found. The voice rules forbid em dashes.')
    lines = ['import type { BlogPost } from "./types";', '', 'export const post: BlogPost = {']
    for key in ORDER:
        if key in meta:
            lines.append(f'  {key}: {json.dumps(meta[key], ensure_ascii=False)},')
    content = body.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    lines.append('  content: `\n' + content + '\n`,')
    lines.append('};')
    name = os.path.splitext(os.path.basename(src))[0]
    out = os.path.join(ROOT, 'copy', name + '.ts')
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(f'Wrote {os.path.relpath(out, ROOT)}: {words} words, readTime {meta["readTime"]}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
