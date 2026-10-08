# LR Question Type Map: channel content

New takes on the LR Question Type Map guide (`LR-Map-Guide-fixed.html`) for five channels, each made twice: once by an Opus agent with broad latitude, and once by a Haiku agent with a tightly specified brief. Every piece is a standalone HTML page that exports its images.

## Open these

Each file in `dist/` is self-contained (fonts, logo and export code inlined). Open it in a browser, straight from disk.

| Channel | Opus track | Haiku track | Paste-ready text |
|---|---|---|---|
| Blog post (live-site layout) | `dist/opus-blog.html` | `dist/haiku-blog.html` | `copy/opus-blog.ts`, `copy/haiku-blog.ts` (BlogPost modules) |
| Reddit image post (4:3) | `dist/opus-reddit.html` | `dist/haiku-reddit.html` | `copy/*-reddit.md` |
| Facebook post and caption | `dist/opus-facebook.html` | `dist/haiku-facebook.html` | `copy/*-facebook.md` |
| Instagram carousel | `dist/opus-instagram.html` | `dist/haiku-instagram.html` | `copy/*-instagram.md` |
| YouTube storyboard | `dist/opus-youtube.html` | `dist/haiku-youtube.html` | `copy/*-youtube.md` |

## Exporting images

Every page has the same toolbar: choose PNG, JPEG or WebP and a scale (1x true size, 2x, 3x), then use **Export all images (ZIP)**, a set's **Download set as ZIP**, or the PNG/JPG/WEBP buttons under any single image. Text blocks have a **Copy text** button.

## Blog posts

The blog pages render the post with the live site's own blog stylesheets (`kit/site-blog.css`, copied from Business_Planner `client/src/sunlit/public/design09/` and `public.css`) and a preview copy of the site's article reader (`kit/site-reader.js`). The `.ts` files are ready for `apps/germainetutoring-website/client/src/data/posts/`. Before publishing either one:

- The LR Question Type Map was taken off the site on 2026-10-03 and sits in `unpublishedPosts` in `client/src/data/posts/index.ts`. Publishing means replacing `lr-question-type-map.ts`, moving it into `blogPosts`, and restoring its routes and sitemap entries.
- `date` is a placeholder (`2026-10-15`). Posts go live at midnight America/Chicago on their date.
- The share image must be exported and saved at the `social_image` path in the module.
- The social copy links to `/blog/lr-question-type-map` and `/resources/lr-question-type-map`; those pages need to be live before the posts go out.

## How it is built

- `src/` holds the authored pages. They reference the shared kit in `kit/` (`gt-export.js`, `gt-kit.css`, fonts, logo, vendored html-to-image 1.11.13 and JSZip 3.10.1).
- `python3 -I tools/build.py src/<name>.html` writes the standalone `dist/<name>.html`.
- `NODE_PATH=$(npm root -g) node tools/check.js dist/<name>.html` exports every image through the page's own export code into `.checks/<name>/` (ignored by git) and fails on console errors, missing fonts, failed exports or horizontal scroll on a phone.
- `python3 -I tools/blog_to_ts.py src/<model>-blog.html` turns a blog preview into its `BlogPost` module.
- `source/` holds the text extracted from the original guide and every original graphic rendered to PNG. `briefs/` holds the exact instructions each agent received (Haiku briefs embed all their source text so each agent read one file).
