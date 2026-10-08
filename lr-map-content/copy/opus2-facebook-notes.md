# Facebook post, round 2 (Opus): critique and changes

## Round 1, Opus track (`dist/opus-facebook.html`)

What it does well:

- It is the only round-1 version that demonstrates the distinction instead of defining it. It uses the source’s checked library and Model L example, and every claim matches the source slides.
- The discussion prompt has a definite answer, and a reply is ready for it. The first comment says the argument is an original teaching example.
- The alt text is complete.

What is weak:

- Image 1 states the three verdicts but shows none of the reasons. Why the $1,000 cap is not required sits in the smallest line of the last card, and the reader has to do the arithmetic. The source calls this the most useful check.
- The dark argument box is the heaviest element in the frame, so the eye lands on the setup rather than the lesson. Three equal cards follow. At about 120 words with body text at the 28px minimum, the verdict lines are about 10px tall on a phone feed.
- The caption (about 360 words) restates the image card by card, so a reader who taps “See more” gets the image again.
- The prompt (“Model L adds no maintenance cost at all”) has the same answer as the $1,000 cap already shown: sufficient, not required. It tests nothing the image did not already show.
- Image 2’s 2×3 grid puts Critique (2 types) beside Change (6 types), so the lower part of the Critique card is empty. “Evaluate · Weaken” shares a line while every other type has its own. Nothing ties the map to the post.

## Round 1, Haiku track (`dist/haiku-facebook.html`)

What it does well:

- It covers both sets of standards the source Facebook copy names (helpful, required, sufficient; possible, supported, guaranteed, contradicted). The text stays close to the source, and every definition is correct.
- The band header and chip rows are clean and on brand.

What is weak:

- It is a glossary, not a lesson. With no example it names the distinction and stops, so the voice’s teaching pattern (diagnose, distinguish, rule, demonstrate, next action) ends at step two.
- “Possible: The stimulus does not rule it out. That alone proves nothing.” is vaguer than the source’s actual point (an unknown claim is not automatically false; a claim that could fail is not guaranteed). It also sits in a row where every other row names a question type.
- Two equal panels of equal rows give no focal point below the headline. The 250px chip column leaves a wide empty gutter.
- The links appear in both the caption and the first comment. The prompt (“Which two standards do you mix up most often?”) asks for reader history and gives nothing to teach from in a reply.
- The alt text lists the labels but leaves out the definitions.

## What this version changes, and why

1. One chart carries the lesson. Each answer is drawn as the range of added maintenance it allows, against the zone where total costs fall (under $4,000). A bar that stays inside the zone is sufficient. A bar that covers the whole zone is required. The key states the pair in words that mirror each other: “Every amount the answer allows cuts costs” and “The answer allows every amount that cuts costs.” The image now shows why each verdict holds, not just which verdict it is.
2. The prompt is the chart’s third row, and its answer completes the set. The $1,000 cap is sufficient but not required, “less than $4,000” is both, and “less than $5,000” is required but not sufficient. Readers can test their answer with the same picture. A reply image (image 3) resolves the row with two concrete numbers.
3. The one new statement was checked. Everything else comes from the source’s checked slides. For “less than $5,000”, let M be the added maintenance; the conclusion holds exactly when M is under $4,000. Required: if the conclusion holds, M is under $4,000 and so under $5,000. Negated, M is $5,000 or more and total costs rise by at least $1,000. Not sufficient: M = $4,500 satisfies the statement and total costs rise $500.
4. Helpful stays off the chart on purpose. A fact about three other libraries says nothing about this library’s range, so as a bar it would have to cover the whole axis and would read as “required”. The caption handles Strengthen in two sentences instead, which keeps the chart’s rule exact.
5. The caption teaches what the image cannot. It keeps the source’s opening line, the two lists of standards and the map sentences. It explains the two tests with numbers, without repeating the image row by row. It adds the source’s caution that a negated necessary assumption does not have to make the conclusion false: because this example fixes every other cost, its numbers could otherwise teach that. The links appear only in the first comment.
6. The headline sits in a dark band and the argument in a light card, as in the source slide system. The eye goes from headline to chart, not to the setup.
7. The map is a full-width list. Each row is sized to its content, so no card is left part-empty. Family 4 is marked “In this post”, with its three types from the post highlighted, and family 6 is set apart as relationship tasks. The source’s guiding question stays on every row.
8. Legibility and glyphs. Chart labels and tags are 24px and row labels 32px. Every board was checked at full size and at a 400px feed width. There is no ≠, no arrows and no CSS counters: the threshold and ranges are drawn with boxes, and every number is literal text.

Not re-verified: this session could not read the Business_Planner repo (git commands were blocked here, and the checkout has no working files on disk). The note that the two links will not resolve until the new article and guide are live comes from round 1’s reading of the site code.
