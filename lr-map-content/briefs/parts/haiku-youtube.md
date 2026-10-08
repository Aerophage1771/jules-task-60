## Your deliverable: a YouTube video storyboard

A storyboard for an 8 to 10 minute teaching video, plus a thumbnail and the upload copy. Arc: preview, teach, demonstrate, recap.

Page layout: each scene is one row: a 16:9 frame artboard (1920×1080) on the left, the scene notes on the right (stack them on phones). Put all scene rows inside `<section class="gt-set" data-set="Storyboard frames (1920×1080)" data-zip="haiku-youtube-frames">`. Each row is `<div class="scene">` containing `<div class="scene-frame"><div class="gt-artboard frame" data-name="scene-01" data-w="1920" data-h="1080">...</div></div>` and `<div class="scene-notes">...</div>`. Use CSS grid on `.scene` with `grid-template-columns: minmax(0,3fr) minmax(0,2fr)` and one column under 800px. Give `.scene-frame` `min-width:0`.

Scene notes, for every scene: `Scene N · mm:ss to mm:ss`, `Purpose` (one line), `Voiceover` (the full spoken script, in Germaine's voice, reusing the source sentences), `On screen` (the exact text on the frame), `Edit and motion` (what animates or is revealed, in order). Timestamps must add up across scenes.

Scenes (13):
1. Cold open (0:00): the three "might not" sentences from the source, revealed one at a time. Frame: three enclosed rows.
2. The promise: "Different Logical Reasoning questions ask you to do different work on an argument." Frame: the map's six family names in a 3 × 2 grid.
3 to 8. One scene per family (Identify the Parts, Describe the Argument, Critique the Argument, Change the Argument, Form Your Own Argument, Argument-Adjacent). Frame: family number and name, the family question, its question types each with its one-line task (from the reference table Task column), and its "What not to do" line in an enclosed box. Voiceover: the source section for that family, trimmed to about 45 to 70 seconds of speech (roughly 110 to 170 words).
9. Worked example setup: the library and Model L lights argument (premises, conclusion, and the gap: net change = M minus $4,000). Frame: premises and conclusion as two enclosed blocks with the gap equation between them.
10. Same argument, three tasks: Evaluate, Weaken, Strengthen, each with its answer from the worked example. Frame: three columns.
11. Same argument, three more tasks: Necessary Assumption, Sufficient Assumption, Principle Strengthen. Frame: three columns; call out "A $1,000 cap guarantees savings, but savings do not require that tight a cap."
12. Using the map in review: "What standard did my chosen answer fail?" with the source's weak and strong diagnosis.
13. End card: `Read or download the LR Question Type Map` with the link text `germainetutoring.com/resources/lr-question-type-map`, and a space for YouTube end-screen elements (leave the right 40% calm and empty, labelled in the notes, not on the frame).

Frames: dark field (#14243B or #344E73) or paper (#F3F6FA), alternate deliberately. Big type: headline 72 to 96px, body at least 40px, labels at least 30px. Logo on every frame, small, same corner. Each frame must read on a phone screen.

Thumbnail: a separate `<section class="gt-set" data-set="Thumbnail (1280×720)" data-zip="haiku-youtube-thumbnail">` with one artboard `data-name="thumbnail"` 1280×720: at most 6 words of headline (for example `20 LR Types. 6 Jobs.`), very large type, one strong graphic element (for example the six family numbers as a grid), high contrast. No face, no fake arrows, no clickbait.

Upload copy (as `.gt-copy` blocks and in `copy/haiku-youtube.md`): `Video title` (under 70 characters, plain), `Description` (2 short paragraphs from the source, then `Chapters` with timestamps matching your scenes, then the two links), `Pinned comment` (the source first comment adapted to video). The .md file also holds the full voiceover script in scene order.
