# LR Question Type Map post, round 2 (Opus track): notes for Germaine

Files: `src/opus2-blog.html` (preview drawn with the live blog stylesheets, plus the share image), `dist/opus2-blog.html` (standalone build), `copy/opus2-blog.ts` (the `BlogPost` module, slug `lr-question-type-map`), and this file.

## Round 1, judged as you would before posting

### Opus round 1 (`src/opus-blog.html`)

What works:

- A six-family table opens the post, each family paired with one question to ask first, and the connected-process paragraph follows it. You see the whole map before the parts.
- It swaps the source’s one-line city example for the library and Model L argument as a six-row table. That example shows more clearly than anything else in the source that helpful, required and sufficient are different standards.
- Every table has three columns, so the live reader stacks them into cards on a phone instead of scrolling sideways.
- It links the Weaken post, drops the “next post” line (no such post exists), and its share image has a clear focal point in the Design 09 look.

What is weak:

- The Main Conclusion test was reworded to “follow the support until it reaches a claim that supports nothing further.” A background sentence or an opposing view also supports nothing further. The test needs “receives support.”
- The practice list says “Required is not sufficient.” Read as a rule, that contradicts the post’s own example, where the $4,000 threshold is both.
- The 20-type table drops the method and keeps a Task column that repeats the family sections, so it adds little.
- The frequency figures take up two paragraphs after the review advice, where they read as a tangent.
- Form Your Own Argument gets no example. That family’s distinction (possible, supported, guaranteed, contradicted) is the hardest one to see.
- Share image: the type counts (2, 2, 2, 6, 4, 4) carry no meaning for a viewer, and the thin connectors barely read as a route at feed size.

### Haiku round 1 (`src/haiku-blog.html`)

What works:

- It stays closest to the source. Every source sentence is there, including the full reference table with task, method and wrong-answer pattern.
- The resource card comes early, and the share image is plain but legible.

What is weak:

- The four-column table becomes a “wide” scroll box in the live reader. On a desktop the wrong-answer column sits behind a scrollbar, and on a phone the table still scrolls sideways. The most useful reference in the post is the hardest part to read.
- It keeps “That is where the next post begins,” which points to a post that does not exist. It also keeps “The Weaken examples” without a link, which only makes sense to someone who saw the social series.
- The largest family is still taught with the one-sentence city example.
- “What not to do: Choose a statement…” reads as an instruction to do the wrong thing.
- The question for Change the Argument (“helpful, required, or sufficient?”) leaves out Evaluate and Weaken.
- Share image: a numbered list with no structure, so the sixth family looks like the other five, and a wide empty band in the middle.

## What this version changes, and why

1. **Same spine, cleaner joins.** I kept the source wording wherever it works. The one-line lead sentences (“Start by figuring out…”, “Now ask whether…”) are merged into the paragraphs they introduce, and “What not to do” is now “The mistake to avoid.”
2. **The Main Conclusion test keeps its exact meaning.** It now reads: “Follow the support until you reach the claim that receives support and is not used to support anything else.” The older map states the same rule. Two other source words were reworded only because each contains a banned hype word inside it. The meaning is unchanged: for example, a necessary assumption “might not be enough to prove the conclusion.”
3. **The gap is made visible.** A three-row table ($1,000, $4,000, $5,000 of added maintenance) shows the threshold, including break-even. You can check all six verdicts in the worked example against a number.
4. **New: one set of facts, four relationships.** Under Form Your Own Argument, the library premises plus the Strengthen answer (as a third fact) produce four claims: one guaranteed, one supported but not guaranteed, one possible but unknown, one contradicted. I tested each against its standard:
   - The guaranteed claim holds whenever maintenance stays under $4,000.
   - The “probably reduce” claim rests on comparable libraries, and this library could differ.
   - Purchase price never appears in the facts.
   - “Less than $4,000” contradicts “exactly $4,000.”

   The table says which question each claim could answer. It does not call the “probably” claim the Most Strongly Supported answer, because a guaranteed claim would have stronger support.
5. **The reference table is rebuilt around your review question.** The columns are Type, “The correct answer must,” and Wrong-answer pattern to check, grouped by family. The middle column comes from the guide’s task-standards desk reference (its “Required” lines, rephrased to start with verbs). The last column is the guide’s reference table, word for word. With three columns it stacks on a phone.
6. **Practice step 3 is now precise:** “Required does not mean sufficient, and supported does not mean guaranteed.” The post ends with the guide’s own next action, then the consultation: on your next miss, state the standard before you reread the choices, then name the requirement your answer failed.
7. **One frequency figure, placed where it changes a decision.** Change the Argument is 37% of the 5,002 released LR questions in your explanation library (PrepTest 1 through 159). The number comes from the older post’s map data and is the only number used. The fixed guide says no percentages are needed. If you prefer that framing, delete the sentence that starts “This is the largest family”; nothing else depends on it.
8. **Links.** The post links to:
   - `/blog/7-common-weaken-formats`
   - `/blog/complete-lsat-flaw-list`
   - `/blog/necessary-assumption-key-ingredients-defenders` (live 2026-10-09, before this post’s date)
   - `/resources/lr-question-type-map`
   - `/contact`, the convention in current posts, which the reader maps to the consultation page
9. **Left out of the older post on purpose:**
   - “The trap that catches the most students,” which has no evidence behind it.
   - The “How it’s asked” stem lists. They are useful, but at least one stem listed under Principle: Generalize (“best illustrates the proposition”) describes the rule-to-case direction of Principle: Apply, so the lists need a check before reuse.
   - “What Changed from the Cheat Sheet,” which repeats the cheat sheet’s old title, and that title uses a banned hype word.
10. **Format.** The post uses only blocks the live reader styles itself: paragraphs, headings, the resource card, square-key and numbered lists, blockquotes, and three-column tables. There are no figure images and no special classes.

## Share image (`social-image`, 1200 by 630)

The image uses the Design 09 look: the dotted field inside a gold stitched frame, the gold kicker plate, a Merriweather title, and a white plate pressed on an ink shadow. The plate draws the map’s real structure. The first five families are joined in order by arrows, and Argument-Adjacent sits apart in its own gold-wash box, as in the guide’s connected-process chart and the post’s card art. It shows no counts and no percentages. I checked it scaled to 500px wide, about feed-preview size, and the title and all six family names stay readable. The smallest text is 24px.

Export it from the preview at 1x and save it over `public/images/resources/lr-question-type-map/lr-question-type-map-social.png`. Three places use that path, so one file covers all of them:

- the post’s `social_image`
- the resource page (`SOCIAL_IMAGE_URL` in `client/src/pages/LrQuestionTypeMapResource.tsx`)
- `LR_SOCIAL_IMAGE_URL` in `scripts/generate-static-route-entrypoints.mjs`

The file at that path today is the old card, which shows share percentages.

## To publish (from `apps/germainetutoring-website`)

1. Replace `client/src/data/posts/lr-question-type-map.ts` with `copy/opus2-blog.ts`. The new module holds its own HTML, so nothing imports `client/src/content/lr-question-type-map/article-markup.ts` any more, and only the old test still uses `map-data.ts`.
2. In `client/src/data/posts/index.ts`, move `lrQuestionTypeMap` out of `unpublishedPosts` and into `blogPosts`, first in the array (it has the newest date). Leave `unpublishedPosts` empty and update its comment.
3. Rewrite `client/src/data/posts/lr-question-type-map.test.ts`. It currently expects:
   - the post to be unpublished and dated 2026-10-01
   - h2s of Overview, the six families and Quick Reference
   - a numbered h3 for every type
   - a `featured_image`

   The new post has:
   - `social_image` and `social_image_alt`, and no `featured_image`
   - these h2s: The Six Families at a Glance; 1. Identify the Parts through 6. Argument-Adjacent; All 20 Types: What the Answer Must Do; How to Use the Map in Practice
   - two h3s: One Argument, Six Tasks; One Set of Facts, Four Relationships

   It meets the test’s other limits: title 24 characters, snippet 133 (the test wants 110 to 150), meta description 141 (155 or fewer), no em dashes, and the resource card with its link.
4. Add the resource route to `client/src/App.tsx` and `client/src/perf/PublicApp.tsx`: `<Route path="/resources/lr-question-type-map" component={LrQuestionTypeMapResource} />`, with a lazy import like `RcQuestionTypeMapResource`. The page component already exists. Then retire `client/src/pages/lr-question-type-map/publishing-contract.test.ts`, which asserts that the route and the sitemap entries are absent.
5. In `scripts/generate-static-route-entrypoints.mjs`, move both `UNPUBLISHED_ROUTE_METADATA` entries back into `STATIC_ROUTE_METADATA`, then update the blog entry:
   - `title` and `ogTitle`: `metaTitle` + “ | Germaine Tutoring”
   - `description` and `ogDescription`: `metaDescription`
   - the Article `description`: `snippet`
   - `imageAlt`: `social_image_alt`
   - `publishedTime`, `datePublished` and `dateModified`: the post date
6. Uncomment the two LR redirects in `netlify.toml` (around lines 247 to 257). Add `/blog/lr-question-type-map` and `/resources/lr-question-type-map` to `client/public/sitemap.xml` beside the RC map entries.
7. **Resource page.** Three places still promise “the task, method, and most common trap”:
   - the hero deck in `client/src/content/lr-question-type-map/resource-hero.html`
   - `DECK` in `LrQuestionTypeMapResource.tsx`
   - `LR_DECK` in the static-route script

   The PDF and the `page-N.webp` previews are also the older 13-page map, with stem wording and trap names. The post’s card promises the task, the method and the wrong-answer pattern. Regenerate the PDF and previews from the fixed guide, then update `PAGE_DESCRIPTIONS` and “Page 1 of 13.” If you can’t do that yet, at least change “most common trap” to “wrong-answer pattern.”
8. **Card art.** `client/src/sunlit/public/blog/artwork/lr-question-type-map.tsx` exists and is registered. It draws the six families as a trail, with stops sized by share, a bridge before the fifth, and the sixth on a spur, which matches this post. It has no entry in `artwork/selection.json`, so Print shows. The active blog look is `default`. The newyorker and quanta looks have no art for this slug, so add some only if you switch looks. The live article shows the card art above the body; the preview leaves it out.
9. The LR cheat sheet post does not link to the map, and the old test asserts that. If you want the link, add it and change that assertion.
10. **Date.** 2026-10-15 is the brief’s placeholder, a Thursday. The guide gives no date, and nothing in the repository schedules this post. The two latest posts go live on 2026-10-09 and 2026-10-11. Posts go live at midnight America/Chicago on their date.
11. Regenerate `metadata.generated.json` with the normal build. Round 1 also named GT Admin’s built-in post snapshot, its test, and the predeploy smoke list. I could not open the Admin files in this session, so check those before release.
12. Add a CHANGELOG entry. Run `npm run check`, `npx vitest run` and `npm run content:test`.

## Preview notes

- The full-article export is a review image, not something to post.
- Three preview-only rules sit outside the post content and change nothing on the site:
  - The numbered list prints 01 to 03 in the export, because the export cannot evaluate CSS counters.
  - The two “Back to The Fix” buttons stay on one line.
  - The three-column tables are drawn without their scroll box. The export renderer measures text a few pixels wider than a browser does, which drew false scrollbars on the 20-type table. In a browser every table fits, both at 1280px and at 390px.
- `tools/check.js` prints `OK: 2 artboards exported, no console errors.` I inspected both exports at full size and a full-length 390px phone render. Every table stacks into labelled cards on a phone, and the page has no horizontal scroll.
