# Brief: YouTube storyboard (Haiku track)

You are one of ten agents making Germaine Tutoring content from one source: the LR Question Type Map. You own exactly one page. Five agents make the same five pieces on a separate track; you will not see their work and must not look for it.

## Goal

Make a new, improved YouTube storyboard from the source text below. It is not a repair of the original: it is a better take that keeps the source wording wherever the wording already works (reuse sentences verbatim when you can, and edit only to fit the format or to sharpen it). Deliver it as one HTML page whose images export as PNG, JPEG or WebP.

Working directory: `/home/user/jules-task-60/lr-map-content`. Run every command from there.

## Your files (write only these)

- `src/haiku-youtube.html` (you write it)
- `copy/haiku-youtube.md` (you write it: every piece of post text, paste-ready, under clear headings)
- Written by the tools, not by you: `dist/haiku-youtube.html`, `.checks/haiku-youtube/`

## Boundaries

- Read only: this brief, the reference images listed below, `src/_template-blog.html` (blog only), and your own outputs in `src/`, `copy/` and `.checks/`.
- Never read `kit/*.css`, `kit/vendor/*`, any `dist/*.html` file, the original guide, or other agents' files. They are huge or not yours.
- Never edit `kit/`, `tools/`, `source/` or `briefs/`. Do not run git.
- Context budget: stay well under 100k tokens in total. Write the page with one Write call, then fix problems with small Edit calls. Do not re-read your whole page after writing it. Read each reference image once, and at most 4 check images in total.

## Reference images

- `source/renders/day-3__lr-map__slide-01.png`
- `source/renders/presentations__lr-one-argument-six-tasks__03.png`

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

## Brand system for social graphics

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
<body data-export-name="haiku-youtube" data-kit-title="SHORT TITLE FOR THE TOOLBAR">
<header class="page-intro"> what this page is and how to post it, in 2 or 3 sentences </header>

<section class="gt-set" data-set="SET NAME (size)" data-zip="haiku-youtube">
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

## Build and check (required)

Run from `/home/user/jules-task-60/lr-map-content`:

```bash
python3 -I tools/build.py src/haiku-youtube.html
NODE_PATH=$(npm root -g) node tools/check.js dist/haiku-youtube.html
```

`build.py` writes the standalone `dist/haiku-youtube.html` (kit, fonts and logo inlined). `check.js` exports every artboard through the page's own export buttons' code path into `.checks/haiku-youtube/` (1x PNGs) plus `page-desktop.png` and `page-phone.png`. It exits with a PROBLEMS list if anything fails: fix every line and rerun until it prints `OK`.

Then look at the exported PNGs and fix: text that is clipped or overflows, overlapping elements, cramped or empty areas, text too small to read on a phone, anything that touches an edge.

## Done means

1. `tools/check.js` prints `OK` for `dist/haiku-youtube.html`.
2. You looked at the exported images and fixed what you found.
3. No em dashes anywhere in your files (search for the character before you finish).

Reply with: the files you wrote, each artboard's name and size, the final check line, and two or three sentences on what this version does better than the original.

---

# Source text (everything you need; do not open the original files)

## From post.md

### Source post: The LR Question Type Map

Exact text of the Post section in LR-Map-Guide-fixed.html (item lr-map). Title: The LR Question Type Map. Deck: Know the task before you judge the answer. Six families organize all 20 types.

Different Logical Reasoning questions ask you to do different work on an argument. If you do not identify that work before evaluating the choices, you can pick an answer that is true, helpful, or logically interesting and still get the question wrong.

A statement that strengthens an argument might not be necessary to it. A necessary assumption might leave the conclusion unproven. An accurate description of a sentence might name its topic without identifying its role.

These are differences in the task. They should change how you approach the question.

The Weaken examples showed several tools you can use to attack an argument. This map places that work in the larger process. Before you can weaken an argument, you need to know what the author is claiming, what supports that claim, and what the support fails to establish.

I organize the 20 question types into six families. The first five follow the work of analyzing an argument and then drawing a conclusion yourself. The sixth covers questions involving two speakers, a rule and a case, or facts that seem difficult to reconcile.

#### 1. Identify the Parts

**Question types: Role in Argument and Main Conclusion.**

Start by figuring out what each statement is doing.

On a Main Conclusion question, you need the claim the author is ultimately trying to establish. A sentence does not become the main conclusion because it comes last or follows “therefore.” An intermediate conclusion receives support and then helps support another claim.

A useful check is to take two candidate conclusions and ask which one the author uses as a reason for the other. Follow the support to the claim the argument is ultimately defending.

On a Role in Argument question, identify the main conclusion first. Then locate the quoted statement relative to it. Is that statement evidence, an intermediate conclusion, a concession, an opposing view, or background?

Check both parts of the answer: the role it names and the claim it says the statement relates to. “A premise” might be the right role while the rest of the description misstates what that premise supports.

**What not to do:** Choose a statement because it is important or true. You are identifying its job.

#### 2. Describe the Argument

**Question types: Method of Reasoning and Parallel Reasoning.**

Once you know the parts, describe how they work together.

For Method of Reasoning, remove the topic and state the move in plain language. The author might eliminate alternatives, compare two cases, apply a rule, or show that a proposed explanation conflicts with a fact.

Then read each answer as a set of claims about the stimulus. If it says the author cites an expert and questions that expert’s motives, both things need to happen. An answer can start accurately and finish with a move the author never makes.

Parallel Reasoning asks you to find the same structure in a different argument. You might begin with a simple description, such as “a rule is applied to a case.” If several choices fit, compare the relationships more closely: the conditions, the direction of support, and the force of the conclusion.

**What not to do:** Match topics or familiar words. Two arguments about doctors can reason differently. An argument about a museum can use the same reasoning as one about a forest.

#### 3. Critique the Argument

**Question types: Flaw and Parallel Flaw.**

Now ask whether the reasoning works.

For Flaw, identify the specific problem before trying to recognize it in abstract answer wording. What did the author need to establish but leave open? What could be true about the situation that would expose the weakness in the inference?

Then translate each answer back into the stimulus. If an answer says the argument confuses a requirement with a guarantee, identify the requirement and the claimed guarantee. If you cannot locate that error in the reasoning, knowing the name of the fallacy is not enough.

Parallel Flaw adds a matching task. The correct answer must fail in the corresponding way. Another bad argument is not necessarily a parallel bad argument.

**What not to do:** Pick a familiar flaw because it is a real flaw. It must be the flaw this argument commits.

#### 4. Change the Argument

**Question types: Evaluate, Weaken, Strengthen, Sufficient Assumption, Necessary Assumption, and Principle Strengthen.**

These types often begin from the same gap. They ask you to do different things with it.

- **Evaluate:** Find information that would help you judge the reasoning. Consider contrasting answers to the proposed question. Would they change your assessment of the argument?
- **Weaken:** Find a fact that reduces the support for the conclusion. Preserve the given evidence and show why it may not establish what the author claims.
- **Strengthen:** Find a fact that improves the support for the conclusion. Address the actual inference, rather than merely adding something favorable about the topic.
- **Sufficient Assumption:** Add a statement that makes the conclusion follow. Put it together with the premises and check whether any gap remains.
- **Necessary Assumption:** Find something the argument requires. Negate a candidate precisely and ask whether the reasoning still has the support it requires. You do not have to show that the conclusion itself becomes false.
- **Principle Strengthen:** Find a general rule that helps justify the conclusion in this case. Connect the facts, the rule, and the conclusion. Increased support is enough unless the question asks you to make the conclusion follow.

Suppose the author offers evidence about how well a plan worked in one city and concludes that it will work in another. A difference between the cities may weaken the inference. A relevant similarity may strengthen it. A question about that difference may help evaluate it.

That shared starting point does not make the tasks interchangeable.

**What not to do:** Use “this helps” as the standard for every question in the family. Helpful, required, and sufficient are different.

#### 5. Form Your Own Argument

**Question types: Fill in the Blank, Most Strongly Supported, Must Be True, and Must Be False.**

Here the task concerns what the statements support, complete, or rule out.

On Most Strongly Supported, look for the claim with the best support in the information provided. You should be able to point to that support. A claim can be plausible in the real world without being supported by this stimulus.

Must Be True asks for a guarantee. Try to make the answer false while leaving the stimulus true. If you can do that, it is not required by the facts.

Must Be False asks for the opposite relationship: an answer that cannot coexist with the given information. Something the stimulus never discusses is not automatically false. It may simply be unknown.

Fill in the Blank requires another preliminary check. What is the missing statement doing? A conclusion needs support from what came before. A missing premise needs to perform the work the surrounding argument requires. Use the sentence and the question wording to identify that job before choosing a completion.

**What not to do:** Treat possible, supported, guaranteed, and contradicted as the same judgment. They are four different relationships to the evidence.

#### 6. Argument-Adjacent

**Question types: Agree / Disagree, Principle: Apply, Principle: Generalize, and Paradox.**

These questions involve relationships that need their own checks.

For Agree / Disagree, establish each speaker’s position on the exact statement in the answer. Silence is not disagreement. If one speaker’s view is unknown, you do not yet have the required relationship.

For Principle: Apply, break the rule into its conditions and result. Then check the case against each condition. Meeting most of a rule’s requirements is not meeting all of them.

Principle: Generalize reverses the direction. Start with the case and identify the broader rule or relationship it illustrates. A principle about the same subject can still misdescribe the case.

For Paradox, state what is surprising: “We would expect this, but instead that happened.” A correct explanation lets both given facts remain true and makes their coexistence less surprising.

**What not to do:** Ignore one side of the relationship. Check both speakers, the rule and the case, or both facts in the apparent conflict.

#### How to Use the Map in Practice

When you begin a question, identify its type and state the task in ordinary language.

Then choose the appropriate tool. Sometimes that is a full prephrase. Sometimes it is an abstract structure. Sometimes it is a gap, a rule, or a contradiction you need to test against the choices.

You do not have to predict the exact wording of every correct answer. You do need to know what work the answer has to do.

When you review a miss, use the same map to ask a more precise question:

> What standard did my chosen answer fail?

“Wrong answer” is not much of a diagnosis. “I picked something that strengthened the argument when I needed something the argument required” tells you what to change.

That is where the next post begins. Knowing the task helps you justify the right answer. It also tells you exactly why the tempting alternatives fail.

[Read or download the LR Question Type Map](https://germainetutoring.com/resources/lr-question-type-map).

If you can identify the question type but keep choosing answers that miss its standard, bring a recent example and your reasoning to a [free consultation](https://germainetutoring.com/#consultation). We can examine where your process needs a more specific step.

## From reference-table.md

### Source reference table

Exact text of the By question type section in LR-Map-Guide-fixed.html.

### All 20 Logical Reasoning Question Types

Use the task to select the method. Use the trap as a check, not as a substitute for reading the actual argument.

| Type | Task | Method | Wrong-answer pattern to check |
| --- | --- | --- | --- |
| Role in Argument | Identify the job of the quoted statement. | Find the main conclusion; trace what the statement supports, is supported by, or sets aside; verify the role and its relationship. | Correct role paired with the wrong claim or relationship. |
| Main Conclusion | Identify the claim the author is ultimately defending. | Compare candidate claims and follow the support; separate the final claim from a conclusion used to support it. | An intermediate conclusion presented as the main one. |
| Method of Reasoning | Describe how the argument proceeds. | State the reasoning move without the topic; translate every part of an answer back into the stimulus. | A partly accurate description that adds a move never made. |
| Parallel Reasoning | Match the reasoning structure. | Abstract the structure; compare the conclusion’s force and the relationships that produce it. | Same subject or vocabulary, different logic. |
| Flaw | Identify the error in the reasoning. | Name the gap; translate the proposed criticism into the stimulus’s terms; check that it describes the actual inference. | A real flaw that this argument does not commit. |
| Parallel Flaw | Match the relevant flawed reasoning. | Identify the stimulus’s error first; then check that the answer makes the corresponding faulty move. | A different flaw hidden beneath a similar topic or shape. |
| Evaluate | Find information useful in assessing the argument. | Identify the gap; try contrasting responses to the proposed question; check whether the argument’s support changes. | A question about the topic whose answers do not resolve the reasoning issue. |
| Weaken | Reduce the support for the conclusion. | Identify the evidence, conclusion, and gap; accept the choice as true; explain how it damages the inference. | Harm to a side issue while the relevant support remains intact. |
| Strengthen | Improve the support for the conclusion. | Identify the gap; accept the choice as true; state the specific improvement it makes to the inference. | Repeated evidence or favorable information that adds no support. |
| Sufficient Assumption | Make the conclusion follow when the answer is added. | Locate the missing connection; add the choice to the premises; test whether the conclusion now follows. | The right terms linked in the wrong direction, or an answer leaving another gap. |
| Necessary Assumption | Identify what the argument requires. | Locate the dependency; negate a candidate accurately; test whether the reasoning survives. | A helpful or sufficient statement the argument does not need. |
| Principle Strengthen | Supply a general rule that helps justify the conclusion. | Connect the facts to the rule and its result to the conclusion. Test for added support; require a guarantee only when the stem asks for one. | A rule with no supported connection to this case or its conclusion. |
| Fill in the Blank | Complete the passage in the role the blank requires. | Determine whether the blank is a premise, conclusion, or other needed statement; follow the surrounding reasoning and the stem’s standard. | A completion on the right topic that does not perform the missing job. |
| Most Strongly Supported | Identify the claim with the strongest support from the stimulus. | Combine the relevant statements; locate support for the answer; reject claims that require unsupported additions. | Plausible in ordinary life but unsupported here. |
| Must Be True | Identify a claim guaranteed by the statements. | Link relevant facts; try to keep the stimulus true while making the answer false. | A claim that could fail without contradicting the stimulus. |
| Must Be False | Identify a claim incompatible with the statements. | Add the choice to the given facts; locate the contradiction it creates. | An unknown or unsupported claim mistaken for a contradiction. |
| Agree / Disagree | Identify a shared or opposed position. | Determine what each speaker would say about the same statement; require evidence of both positions. | One speaker addresses it while the other’s position is unknown. |
| Principle: Apply | Identify the case or judgment licensed by a rule. | Translate the rule; check whether its sufficient grounds or necessary requirements support the proposed judgment. | A case that meets only some conditions or reaches an unlicensed result. |
| Principle: Generalize | Identify the principle the case illustrates. | Abstract who did what, under which conditions, and with what result; match each element to the principle. | A rule about the same subject that misstates the case’s relationship or conditions. |
| Paradox: Resolve, Reconcile, Explain | Explain how the surprising facts can coexist. | Name the expectation and surprising result; accept each choice as true; see whether it explains both together. | Denying one of the given facts or explaining only an unrelated detail. |

“Too strong,” “out of scope,” and “new information” are not automatic reasons to eliminate an answer. What counts as a defect depends on the task. A Sufficient Assumption may need a strong rule. Strengthen and Weaken invite new information. An inference may use different wording while remaining supported.

## From alternates.md (worked example only)

#### One argument, six different tasks

An original ten-slide worked case holds the facts fixed and shows exactly how Evaluate, Weaken, Strengthen, Necessary Assumption, Sufficient Assumption, and Principle Strengthen differ.

##### Readable text

### One Argument, Six Different Tasks

This is an original teaching example. Each proposed answer is considered separately.

**Premises:** Replacing a library’s conventional lights with Model L fixtures will reduce its annual electricity bill by exactly $4,000. All other annual operating costs stay unchanged, except that Model L may add maintenance costs.

**Conclusion:** The switch will reduce total annual operating costs.

Let M be the annual maintenance increase. The net annual cost change is M minus $4,000. The conclusion holds exactly when M is below $4,000.

#### Evaluate

Ask how much annual maintenance will increase. A $1,000 increase supports the conclusion; a $5,000 increase defeats it. Contrasting responses change the assessment.

#### Weaken

An added $5,000 annual maintenance cost more than cancels the saving. This weakener actually disproves the conclusion in the specified case. Weakening does not always require disproof.

#### Strengthen

If three libraries with comparable operating hours and the same fixtures incurred maintenance increases under $1,000, that supports a low estimate here. It does not guarantee the estimate, because this library’s conditions could differ.

#### Necessary Assumption

The added annual maintenance cost must be below $4,000. Negate that: $4,000 or more would mean no reduction. In this numerical example, this exact threshold is both necessary and sufficient. Necessity and sufficiency are properties that can overlap.

#### Sufficient Assumption

A $1,000 cap on added annual maintenance guarantees at least $3,000 savings. It is sufficient but not necessary: a $3,000 maintenance increase would still allow savings.

#### Principle Strengthen

A general rule that libraries replacing conventional lights with Model L add no more than $1,000 in annual maintenance applies to this case and supplies a sufficient cap. A rule about another model would not apply merely because its result looks useful.

#### Your next question

State the task before comparing choices. Then write what the chosen answer actually does to the reasoning. A statement may meet more than one standard; the stem determines which property you need to establish.

##### Caption

### Caption

“This helps the argument” is not the test for every question.

A helpful fact might not be required. A required condition might not prove the conclusion. A sufficient condition can go further than the argument needs.

This example keeps one library’s cost argument fixed and changes the task six times. Work out the missing cost comparison, then see what each answer does to it.

The most useful check comes on the assumption slides: a $1,000 maintenance cap guarantees savings, but savings do not require that tight a cap.

Save the comparison and try naming the exact standard on your next missed question.

#### First comment

The scenario is invented for teaching; each slide tests its proposed answer separately.

Full LR map: https://germainetutoring.com/blog/lr-question-type-map

If you can name the question type but keep accepting answers that miss its standard, bring an example and your reasoning to a free consultation: https://germainetutoring.com/#consultation

##### Image descriptions

##### 1. One argument. Six different jobs.

A worked teaching example will hold one argument fixed and compare Evaluate, Weaken, Strengthen, Necessary Assumption, Sufficient Assumption, and Principle Strengthen.

##### 2. The argument we will test.

The library expects an exact 4,000-dollar annual electricity saving; maintenance is the only annual operating cost that may increase. It concludes that total annual operating costs will fall.

##### 3. Name the gap precisely.

The net cost change equals added maintenance minus 4,000 dollars. An increase below 4,000 produces savings; an equal increase breaks even; a larger increase raises total costs.

##### 4. Evaluate: what would you ask?

Evaluate asks for the amount of added maintenance. Answers of 1,000 dollars and 5,000 dollars lead to opposite assessments of the cost-reduction conclusion.

##### 5. Weaken: make the support worse.

An added 5,000-dollar annual maintenance cost exceeds the guaranteed 4,000-dollar electricity saving, so annual costs rise by 1,000 dollars and the conclusion is undermined.

##### 6. Strengthen: add support.

Maintenance experience at three comparable libraries supports a lower maintenance estimate, strengthening the argument without guaranteeing this library’s actual costs.

##### 7. Necessary: what must hold?

The maintenance increase must be below 4,000 dollars. Its negation, 4,000 or more, rules out a reduction. No maintenance increase at all is stronger than required.

##### 8. Sufficient: make it follow.

A maintenance increase capped at 1,000 dollars guarantees at least 3,000 dollars in savings, but that cap is not necessary because a 3,000-dollar increase would also permit savings.

##### 9. Principle: connect rule to case.

A general rule about libraries installing Model L applies to this case and supplies the 1,000-dollar cap. A rule about a different fixture model would fail because its trigger is not established.

##### 10. Test the job, not the label.

Summary distinguishes the six question tasks and emphasizes that one statement can meet multiple standards; correctness depends on the requested task.

## From social-copy.md (first comment only)

### Source first comment

#### First comment

Full article: https://germainetutoring.com/blog/lr-question-type-map

Read or download the guide: https://germainetutoring.com/resources/lr-question-type-map

If you know the type but keep missing what the answer needs to do, bring a recent example and your reasoning to a free consultation: https://germainetutoring.com/#consultation
