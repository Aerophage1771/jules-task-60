# YouTube storyboard, round 2: critique and changes

I rendered both round-1 pages with `tools/check.js` and looked at every exported frame at full size before building this one. Neither has an LSAT error that I could find in the YouTube material, and neither falls into the glyph trap (round 1 Opus drew its ≠ signs as SVG). The differences are in how much each one teaches on screen.

## Round 1, Opus track (`opus-youtube`)

What works. A real arc (cold open, the map, six families, the worked example, a callback, a review routine, an end screen). The cold open is the right hook: one answer that meets the Strengthen and Sufficient standards and fails the Necessary one. The worked example is the best part of either version: one locked layout for all six tasks with a number line that never moves, a six-dot tracker, and accurate verdicts. The production notes (caption advice, music drop-out, end-screen slots, chapter times that match the scene timings) are what an editor needs.

What is weak.
- The family scenes define but never demonstrate. Family 1 shows three empty boxes labelled Premise, Intermediate conclusion and Main conclusion with no sentences in them; family 2 shows chips reading “Doctors, Doctors: can differ” and “Museum, Forest: can match”; family 3 repeats the instruction to “point to the requirement” without a requirement to point to. Only family 4 ever gets an example, so five of six families skip the demonstrate step.
- The frame called “the map” lists the six families and type counts (“2 types”) but not the 20 type names. The one frame a viewer would screenshot doesn’t contain the map.
- The cold open shows the answer and its three verdicts without the argument, so the viewer can’t check the verdicts until seven minutes later.
- The task frames never show the stem or say what the answer must do before the answer appears, and most carry no verdict, so the viewer has nothing to prephrase against and nothing to confirm.
- The cold open and the family 2 frame stop 120 to 140 px above the footer, leaving an empty band.

## Round 1, Haiku track (`haiku-youtube`)

What works. It keeps the source wording almost verbatim, so it is accurate, and every family keeps its “what not to do” line. It is short (9:40) and simple to produce.

What is weak.
- Most frames are text slides read aloud: headline, a paragraph per type, a callout. Nothing is shown that the voiceover doesn’t already say.
- Lopsided and empty frames. The Identify the Parts frame leaves the middle third blank; in the Evaluate, Weaken and Strengthen frame two of three cards are half empty; the six family tiles on the overview are mostly blank space with no type names.
- The worked example is crammed three tasks to a frame with no picture of the gap, which throws away the source’s strongest material.
- The scene timings are evenly spaced (one minute per family, whatever the word count), so the chapters are guesses rather than estimates from the script.
- One thumbnail, “20 LR Types. 6 Jobs.”, with unlabelled tiles numbered 1 to 6. “Jobs” misnames the families (the 20 types each have their own job), and the tiles say nothing at feed size.
- The logo sits top left beside the eyebrow on every frame and several frames use the ink colour as a dark field instead of the band blue.
- No end-screen guidance (no slots or notes for YouTube’s end-screen elements), and the pinned comment repeats the description.

## What this version changes, and why

1. Every family is demonstrated on one running example. A three-sentence bridge argument (cracks, so unsafe, so close it) carries families 1 to 4 and 6: the intermediate conclusion is a real sentence; Parallel Reasoning shows one argument that matches it on a different topic and one that is about the same bridge and reasons differently; Flaw shows one answer the argument commits and one real flaw it doesn’t; Evaluate, Weaken and Strengthen each get a bridge answer; Principle: Apply gets a rule whose condition the case fails. Family 5 gets three statements about Route 9 and four claims labelled guaranteed, supported, contradicted and possible. I tested each claimed answer against its standard; the possible claim uses a different bridge so nothing from the earlier scenes leaks in.
2. The map frame shows all 20 types, five connected families plus the sixth set apart in gold, as in the source.
3. The cold open shows the argument with the answer, so the three verdicts can be checked on the spot, and the eyebrow sets up the question.
4. Each task frame is built for prephrasing. The band carries the task, the standard as the headline and a real stem form; the notes hold the band alone before the answer appears; the side card names the test (try two answers, accept it as true, negate it, add it to the premises, check the trigger) and ends in a verdict badge. The locked number line from round 1 stays.
5. The recap is a three-by-three matrix (the $1,000 cap, the under-$4,000 condition and the three comparable libraries against Strengthen, Sufficient and Necessary). It shows the source’s two points at once: one statement can meet several standards, and necessity and sufficiency can overlap.
6. Scripts, timings, chapters and frames come from one scene list. A small generator writes both the page and the .md, estimates each scene from its word count (dollar amounts counted as spoken), and refuses a chapter shorter than 10 seconds. The chapters can’t drift from the run sheet.
7. Upload copy is paste-ready: title, alternate title, description with 18 chapters, a pinned comment that gives a fill-in review sentence, and a teleprompter script that doubles as the caption source.
8. Two thumbnails at feed size: A repeats the cold open with one-word verdict chips; B puts all six family names on bars beside “20 types. Six families.”
9. Cut: round 1’s agenda card and six-task recap table. The agenda now sits in the title scene’s voiceover, and each task frame’s headline already states its standard, so the matrix replaces the recap.
10. A publishing check in the production notes: the LR map post was taken down on 2026-10-03, so the description, pinned comment and end screen tell the editor to confirm both links are live first.

Craft rules kept: symbols (checks, crosses, arrows, plus) are inline SVG, numbers are literal text, the minus sign renders in Inter, body text is 50 px or larger and labels 40 px on 1920-wide frames, every highlighted box is fully enclosed, and every frame keeps the bottom strip for the logo and the “Original teaching example” label only.
