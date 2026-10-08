# Brief: Instagram carousel (Opus track, round 2)

You are one of five Opus agents making round-2 Germaine Tutoring content from one source: the LR Question Type Map guide. Each agent owns one channel. You own: Instagram carousel.

This is not a repair of the original, and not a restyle of round 1. Make a new, improved take on the source content, keeping its text largely the same where the text already works, and deliver it as an HTML page whose images export as PNG, JPEG or WebP through the shared kit.

Working directory: `/home/user/jules-task-60/lr-map-content`. Do not run git; the orchestrator commits.

## What you have

- The original guide (2.7 MB, mostly embedded fonts): `/root/.claude/uploads/14222cda-2c65-50f9-868c-f1dc09953932/b25c0050-LR-Map-Guide-fixed.html`. Everything useful in it is already extracted for you:
  - `source/post.md` (the main post), `source/reference-table.md` (all 20 types: task, method, wrong-answer pattern), `source/social-copy.md` (Instagram caption, Facebook copy, first comment, original slide descriptions), `source/alternates.md` (three alternate presentations: the connected process, the task-standards desk reference, and the "one argument, six tasks" worked example with the library and Model L lights).
  - `source/renders/*.png`: every original graphic rendered at true size (8 carousel slides, the complete map, and the 14 alternate-presentation charts and slides).
- The live website's code, read-only, at `/home/user/business_planner` (Aerophage1771/Business_Planner). The checkout is partial: read files with `git -C /home/user/business_planner show HEAD:<path>` and list with `git -C /home/user/business_planner ls-tree -r --name-only HEAD <dir>`. Never run checkout, reset, or any write in that repo. Useful paths: `apps/germainetutoring-website/AGENTS.md` (Blog authoring section), `apps/germainetutoring-website/client/src/data/posts/` (post modules, `types.ts`, `index.ts`; `lr-question-type-map.ts` is an older unpublished version of this post, taken down on 2026-10-03 at Germaine's request), `apps/germainetutoring-website/client/src/content/lr-question-type-map/` (that older version's article markup and map data), `apps/germainetutoring-website/client/src/sunlit/public/blog/` (ArticlePage.tsx, articleContent.tsx, card artwork), `apps/germainetutoring-website/client/src/sunlit/public/design09/blog.css` (live blog styles).
- The Germaine Tutoring voice skill: load it with the Skill tool (`anthropic-skills:germaine-tutoring-voice`) before you write copy. The voice summary below is binding either way.
- The shared export kit and tools in `lr-map-content/kit/` and `lr-map-content/tools/` (see the contract below). Four other Opus agents use them at the same time: never edit anything in `kit/`, `tools/`, `source/`, `briefs/`, the round-1 files (anything named `opus-*` or `haiku-*` in `src/`, `copy/` and `dist/`) or another agent's files. If you need extra behaviour, put it in your own page.

## Round 2: beat both existing versions

This channel has already been made twice. Germaine has asked for another swing at it, and your version has to be clearly better than both:

- Round 1, Opus track (broad latitude): `src/opus-instagram.html`, built page `dist/opus-instagram.html`, text in `copy/opus-instagram.*`, brief `briefs/opus-instagram.md`.
- Round 1, Haiku track (tight brief, text kept close to the source): `src/haiku-instagram.html`, `dist/haiku-instagram.html`, `copy/haiku-instagram.*`, brief `briefs/haiku-instagram.md`.

Before you design anything:

1. Read both pages and their copy files. Render both with `NODE_PATH=$(npm root -g) node tools/check.js dist/opus-instagram.html` and the same for `dist/haiku-instagram.html`, then look at every PNG in `.checks/opus-instagram/` and `.checks/haiku-instagram/` at full size.
2. Judge them as Germaine would before posting: accuracy of every LSAT claim and example, whether each image reads at the channel's real display size (a phone feed for social), hierarchy and focal point, density (crowded or empty), voice, and how well each one uses its channel's format. Note what each does well and what is weak.
3. Then build your own version. Take what works from either one freely, fix what does not, and add what neither has if it earns its place. Never edit the round-1 files.

Known round-1 problems to avoid:

- The kit's fonts (Inter, Fraunces, IBM Plex Mono) lack some symbol glyphs, including ≠ and arrows, so those render in a system fallback font in exports. Use words, draw the symbol as inline SVG, or confirm the render.
- CSS counters (`counter()`) render as "00" in exported images. Write numbers as literal text.
- One round-1 example was invented and overstated what a necessary assumption is. Every example must keep the exact distinction (helpful vs required vs sufficient; possible vs supported vs guaranteed vs contradicted). The source's own worked example (the library argument and the Model L lights in `source/alternates.md`) is checked; if you write a new one, test each claimed answer against its standard before you use it.
- Lopsided or empty areas inside a frame (one round-1 storyboard frame left a third of the frame blank). Check every exported image at full size, not only the contact sheet.

Write `copy/opus2-instagram-notes.md`: a short critique of both round-1 versions (what each does well, what is weak), then what your version changes and why.

## Your latitude

You are the "use your judgment" track. The brief below states the goal and the non-negotiables; the structure, the number of images, the layout, the visual direction within the brand, and any added formats are your call. Aim for the version Germaine would actually post: specific, accurate, visually confident, and better than the original in ways you can name. Keep source wording where it already works, and improve it where it does not. You may add extra artboards (variants, alternate sizes) when they are genuinely useful, but the core deliverable comes first and must be finished and checked.

## Goal: an Instagram carousel

A complete Instagram carousel (4:5, 1080×1350 per slide, up to 20 slides) plus the caption, first comment and per-slide alt text. Instagram's register is one rule per slide: a concrete tension or mistake to open, one teachable idea per slide, and a save, practice or reply action to close. The original eight slides are in `source/renders/day-3__lr-map__slide-0*.png`; make a new carousel that teaches more per swipe without crowding, and consider whether the "one argument, six tasks" worked example belongs in it. Files: `src/opus2-instagram.html`, `copy/opus2-instagram.md`.

## Voice: Germaine Tutoring

Write as Germaine Tutoring: a precise, candid, invested LSAT coach who turns ambiguity into repeatable rules and makes the reader feel individually attended to.

Prioritize, in order: specific over generic, clear over impressive, rule-based over intuition-only, personable over institutional, and high-touch over transactional.

Default teaching pattern: diagnose the exact confusion, name the key distinction, state a reusable rule, demonstrate it, then give the next action. Treat the reader as capable. Use "you" for reader action and "I" for Germaine's judgment.

Hard rules:
- Never use em dashes (the long dash). Not in HTML, not in the .md file, not in alt text. Use a period, comma, colon or parentheses instead.
- No hype words: ultimate, masterclass, secret, hack, crush, transform, proven, game-changer. No fake urgency, no clickbait questions, no "Let's dive in", no "It's important to note".
- Do not invent statistics, frequencies, score gains, testimonials or student stories.
- Do not change the meaning of any LSAT rule. When you shorten a source sentence, keep its exact distinction (helpful vs required vs sufficient; possible vs supported vs guaranteed vs contradicted).
- Do not make every paragraph one sentence. Do not use bold as a substitute for clear sentences.
- Keep the source's curly quotes and apostrophes (’ “ ”) consistent.
- The current LSAT has no Logic Games. Never mention Logic Games.

## Brand system (default for social graphics; the blog follows the live site instead)

Use the system of the original graphics (shown in the reference images), but make your own, better layouts.

Colors:
- Band / dark field: #344E73. Brand blue: #3E5F8F. Ink (darkest text): #14243B. Body text: #28364A. Muted text: #5A6B82.
- Paper (page background): #F3F6FA. Wash: #E7EDF5. Card: #FFFFFF. Lines: #C3CEDD.
- Gold accent: #E3C06B. Gold wash (soft highlight fill): #FBF4DF. Gold dark (text on light): #7A5818.
- Use sparingly: pen #A8325E, good #376346, red #984236.

Type (already loaded by the kit, use these exact family names):
- Headlines: Fraunces, weight 550, letter-spacing -0.02em, line-height 1.05 to 1.15.
- Body and lists: Inter, weights 400/500/600/700.
- Eyebrows, labels, slide numbers: 'IBM Plex Mono', weight 500, uppercase, letter-spacing 0.06em.

Logo: `<img class="logo" src="../kit/logo.svg" alt="Germaine Tutoring">` on light backgrounds, `../kit/logo-white.svg` on dark ones. Give `.logo` a height (34 to 48px) and `width:auto`. The build step turns it into inline SVG so it exports.

Layout rules:
- Safe margin of at least 56px inside every artboard. Nothing may touch, cross or clip at an edge.
- Minimum text sizes on a 1080px-wide artboard: body 28px, labels 22px. Scale up proportionally on wider artboards.
- One clear focal point per image. Strong hierarchy: eyebrow, headline, supporting content, footer.
- Never put an accent bar or rail on only one side of a box (no left borders, no top stripes on cards). A highlighted box is enclosed on all sides: a full border, a fill, or a shadow under the whole box.
- No gradients that reduce text contrast. Body text contrast at least 4.5:1.

## Page contract (export kit)

Every page uses the shared kit in `lr-map-content/kit/`. You do not edit the kit; you only reference it. The kit adds the toolbar (format PNG/JPEG/WebP, scale 1x/2x/3x, export all as ZIP), a Download-set button per set, per-image export buttons, preview scaling, and Copy buttons on copy blocks.

Skeleton (keep the link and script tags exactly; paths are relative to `src/`):

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PAGE TITLE</title>
<link rel="stylesheet" href="../kit/fonts-social.css">
<link rel="stylesheet" href="../kit/gt-kit.css">
<style>
  body { margin: 0; background: #E7EDF5; color: #28364A; font-family: Inter, sans-serif; }
  .page-intro { max-width: 860px; margin: 24px auto 0; padding: 0 16px; }
  /* Artboard styles. Scope every rule under the artboard's own class (for example .slide h1),
     use px units only (no vw, vh or %-of-viewport sizing), and lay out with flex or grid. */
</style>
</head>
<body data-export-name="opus2-instagram" data-kit-title="SHORT TITLE FOR THE TOOLBAR">
<header class="page-intro"> what this page is and how to post it, in 2 or 3 sentences </header>

<section class="gt-set" data-set="SET NAME (size)" data-zip="opus2-instagram">
  <div class="gt-artboard slide" data-name="slide-01" data-w="1080" data-h="1350">
    ... content ...
    <img class="logo" src="../kit/logo.svg" alt="Germaine Tutoring">
  </div>
</section>

<section class="gt-copy" data-label="Caption"><pre>Plain text exactly as it should be pasted.</pre></section>

<script src="../kit/vendor/html-to-image.js"></script>
<script src="../kit/vendor/jszip.min.js"></script>
<script src="../kit/gt-export.js"></script>
</body>
</html>
```

Contract details:
- `.gt-artboard` needs `data-name` (kebab-case, used in file names), `data-w` and `data-h` in px. The kit fixes the box to that size with `box-sizing: border-box` and `overflow: hidden`, so anything that does not fit is cut off. Design to fit.
- Artboards that are direct children of a `.gt-set` line up in a grid. An artboard nested inside your own block (for example a storyboard row with notes beside it) stays where you put it.
- `.gt-copy` blocks get a Copy button. Put the paste-ready text inside one `<pre>`.
- Do not add other scripts, external images, web fonts or CDN links. Everything must work offline after the build.

## Build and check (required)

Run from `/home/user/jules-task-60/lr-map-content`:

```bash
python3 -I tools/build.py src/opus2-instagram.html
NODE_PATH=$(npm root -g) node tools/check.js dist/opus2-instagram.html
```

`build.py` writes the standalone `dist/opus2-instagram.html` (kit, fonts and logo inlined). `check.js` exports every artboard through the page's own export buttons' code path into `.checks/opus2-instagram/` (1x PNGs) plus `page-desktop.png` and `page-phone.png`. It exits with a PROBLEMS list if anything fails: fix every line and rerun until it prints `OK`.

Then look at the exported PNGs and fix: text that is clipped or overflows, overlapping elements, cramped or empty areas, text too small to read on a phone, anything that touches an edge.

## Done means

`tools/check.js` prints `OK` for `dist/opus2-instagram.html`, you have inspected the exported images and fixed what you found, and no file of yours contains an em dash. `copy/opus2-instagram-notes.md` holds your critique and changes. Reply with: the files you wrote, your verdict on each round-1 version in two or three lines, each artboard's name and size, the final check line, and a short list of the decisions you made and why.
