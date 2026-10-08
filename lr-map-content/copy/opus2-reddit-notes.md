# Reddit image post, round 2 (Opus): critique and changes

I rendered both round-1 pages with `tools/check.js`, looked at every export at full size, and also scaled each lead image down to 390px wide (roughly how a phone feed shows a 1600px image) to judge the glance read.

## Round 1, Opus track (`opus-reddit`)

What works:

- The lead image makes one checkable claim instead of showing a branded cheat sheet. The yes/no grid reads at phone size: the big Yes/No marks and the gold Required column are visible even at 390px.
- The example comes from the checked source (the library and Model L lights) and the image says it is an original example with answers tested alone.
- The body teaches all six families, keeps source wording where it works, and ends with one plain disclosure line.
- Image 2 (the map) is tidy: stacked family rows, families 1 to 5 joined, family 6 set apart.

What is weak:

- Answer (B) is the exact $4,000 threshold, so it is both necessary and sufficient. The grid shows that a helpful answer isn’t required (A) and that a sufficient answer isn’t required (C), but it never shows a required answer that fails to prove the conclusion. That is the source’s second key sentence (“A necessary assumption might leave the conclusion unproven”). Without it, a reader can still believe that the required answer is the one that makes the argument work.
- The grid gives verdicts without reasons. Zooming in, a reader still can’t see why C isn’t required or why A doesn’t guarantee anything; the deciding numbers are only in the body. The top-left table cell holds a slogan where the gap would do more work.
- Image 2 uses the ≠ glyph, which the kit fonts lack, so it renders in a fallback font. Family questions sit at 33px on the same line as the family name, and the line joining families 1 to 5 is not explained anywhere on the image.
- The title runs about 150 characters and reads as two titles joined together.
- The body (about 1,450 words) is mostly the source post re-paragraphed. Only a few types get a wrong-answer pattern, so the reference table’s most useful column is missing. The closing comment offer commits Germaine to replying to every miss people post.

## Round 1, Haiku track (`haiku-reddit`)

What works:

- The wording stays close to the source, the title is plain and specific, and the body is a compact 410 words that covers the two key distinctions and the review question, with a one-line disclosure.
- The 3 × 2 card grid is orderly and on-brand.

What is weak:

- The image is the complete map shrunk into landscape. Type names are 24px on a 1600px board (about 6px on a phone), well under the brief’s floor (about 41px body and 33px labels at this width). At feed size only the headline reads.
- The cards are lopsided: in the top row, about 40% of each card is empty between the type list and the gold box. The family question (the card’s most prominent element) sits at the bottom, after the types, so each card reads in the wrong order.
- “Helpful ≠ required ≠ sufficient.” uses the ≠ glyph (fallback font).
- There is no worked example, so the body states the distinctions without letting a reader check one. One line is imprecise: “you will miss the ones that ask for something narrower.” Sufficient Assumption asks for something stronger than help, and Necessary Assumption asks for a different relationship, not a narrower one.
- The alt text does not list the 20 types, so a screen-reader user misses the content of the image.
- The image prints `germainetutoring.com/blog/lr-question-type-map`, a page that is currently unpublished, and a URL baked into an image can’t be corrected after posting.

## What this version changes, and why

1. **A new answer set that separates all three standards.** I kept the source’s argument and its checked answers for A (comparable libraries, a strengthener that is neither necessary nor sufficient) and C (the $1,000 cap, sufficient but not necessary), and replaced the exact-threshold B with “less than $5,000.” I tested each claim before using it. With M as added maintenance, costs fall exactly when M is under $4,000. B is necessary: negated (M is $5,000 or more), costs rise by at least $1,000. B is not sufficient: M = $4,500 satisfies B and costs rise by $500. C is sufficient: M of $1,000 or less saves at least $3,000. C is not necessary: M = $3,000 still saves $1,000. A is neither: negated, this library can still save, and with it this library’s cost is still open. All three raise the support. Now the required answer and the guaranteeing answer are different rows, which is the split the source post opens with.
2. **The deciding number is in every cell.** Each verdict carries a short reason (“costs rise at $5,000 or more”, “$4,500 fits it, and costs rise”, “at $3,000, costs still fall”), so a reader who zooms can check the grid without the body. The gap (“Costs fall exactly when added maintenance is under $4,000”) sits in the argument panel, directly above the answers.
3. **One focal point at phone size.** The headline states the whole result (“All three answers help. Only B is required. Only C guarantees the conclusion.”) and stays readable at feed width. The only two passing cells are boxed in gold on a diagonal, so the pattern carries the same message. I dropped the all-yes Helps column and put that result in the first column header (“Helps? Yes, all three.”). That freed the width the answers need to fit on two lines at the 42px floor.
4. **The body teaches more and claims no more.** It adds two rules from the example (don’t eliminate a Necessary Assumption answer for looking too weak; don’t eliminate a Sufficient Assumption answer for saying more than needed), with the source’s caveat that a negation doesn’t have to make the conclusion false. It adds a practice answer (D, the exact threshold, which passes all three tests) behind a Reddit spoiler, and a task plus a wrong-answer pattern for every one of the 20 types from the reference table. I cut sentences that only repeated their own “Watch for” line. The result is about 1,600 words, organized under headers so it can be skimmed.
5. **A cleaner map.** Image 2 puts the family name and question on the left and the types on the right, so each row reads as family, task, types. It has no ≠ glyph, all numbers are literal text, one continuous rail joins families 1 to 5, and the footer says what the rail means (“1 to 5 follow one argument · 6 sits apart”). Family questions use the source’s own slide wording where the complete-map wording would not fit on one line.
6. **No URL on either image, one disclosure line in the body.** The link appears once, at the end, pointing to the free resource page. A posting note says to confirm that the page is live first. The title is 121 characters and states the distinction plainly; the alternates offer a more specific hook and a map-first framing.

Every exported image was checked at full size: nothing clips or touches an edge, no text sits below the size floors (body 42px, labels 33px), and there are no fallback glyphs or CSS counters.
