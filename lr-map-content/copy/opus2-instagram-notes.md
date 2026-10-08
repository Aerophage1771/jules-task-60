# Instagram carousel, round 2: critique and changes

I rendered both round-1 carousels with `tools/check.js` and read every exported slide at full size and at phone feed width (about 390px).

## Round 1, Opus track (`dist/opus-instagram.html`, 13 slides)

What works:

- Every LSAT claim I checked is accurate, and it is the only version that teaches the library worked example. The threshold bar (slide 7) and the nested range chart (slide 9) make the necessary and sufficient difference visible.
- One rule per slide, stated as the headline, with a check and a “Watch for” trap from the source’s wrong-answer patterns.
- A strong cover tension (“True, helpful, and still wrong.”), a save-worthy map with families 1 to 5 connected and family 6 boxed, and a review-worksheet close.
- Symbols are drawn as SVG, and the link wording is consistent (first comment everywhere).

What is weak:

- Density and sameness. Most slides carry 80 to 110 words in the same stack (eyebrow, headline, white card, gold card), so in the feed they look alike and the focal point is a paragraph.
- The family 1 to 3 demonstrations stay abstract. Slide 5’s “translate the answer back” points to “the requirement in the stimulus” with no stimulus on the slide, and the slide 3 support chain has no argument in it.
- Slide 9’s headline, “Required is not the same as enough”, sits over a chart where the required condition (under $4,000) is also enough. The overlap is explained only on the next slide.
- Slide 11 labels Possible “not a standard”, which the source never says.
- The cover names the three standards but never shows an answer being judged by them. The chain-box text on slides 3 and 10 is 23px, below the 28px body minimum.

## Round 1, Haiku track (`dist/haiku-instagram.html`, 10 slides)

What works:

- Closest to the source wording and fully accurate. Slide 2 (“A true answer can still be wrong.”) uses the source’s three best opening sentences, and slide 9 uses the source’s own diagnosis.
- Large, clean type in the original brand layout.

What is weak:

- It teaches the least per swipe. Each family slide restates the type’s task in one line (“Identify the error in the reasoning.”) and adds a one-line “Don’t”. There is no method, example or test, so helpful vs required vs sufficient is asserted and never shown.
- Slides 3 to 5 each have two cards that are about half empty.
- The ≠ (slide 6) and → (slide 1) glyphs render in a fallback font.
- The close is nearly empty and says “Save the map for review” when no slide shows the whole map. It also adds “printable” to the guide and appends hashtags.

## What this version changes and why

- **The cover shows the tension instead of naming it.** One answer choice (“Model L will add no more than $1,000 a year in maintenance.”) meets Strengthen, meets Sufficient Assumption and fails Necessary Assumption. Slides 10 and 11 explain why, and slide 14 reviews that same miss, so the carousel closes the loop it opens.
- **Every family slide has a concrete demonstration.** Family 1: a clinic stimulus with the main conclusion written first and the intermediate conclusion after “so”, which demonstrates the source’s point that a conclusion indicator does not make a claim the main conclusion. Family 2: the source’s museum and forest, written as two arguments with one move. Family 3: a deck permit treated as a guarantee, with the flaw wording translated back into the stimulus’s own words. Family 5: one chess-club stimulus with four claims, one per relationship (possible, supported, guaranteed, contradicted). Family 6: four relationship cards, each with its check and its trap.
- **The worked example is rebuilt on one scale.** Every example slide uses the same $0 to $6,000 maintenance line, with the task’s answer plotted on it. Tasks are paired by contrast (Evaluate with Weaken, Strengthen with Principle Strengthen, Necessary with Sufficient). The new matrix slide shows one statement meeting several standards, which makes the source’s “the stem determines which property you need” visible. The necessary-and-sufficient overlap is stated next to the chart, so no headline claims more than the chart shows.
- **Less text per slide, larger type.** Each slide has one focal visual, and body text runs 28 to 35px. Headlines use balanced wrapping. Every slide’s content ends 24px or more above the footer, and no card is more than a third empty.
- **The close is a filled-in worksheet.** It uses the source’s own diagnosis sentence in “pen”, then asks the reader to explain each wrong answer with that standard, run the same three lines on their next miss, and save the post.
- **Optional story frame.** A 1080 × 1920 version of the cover for sharing the post to Stories, with content kept out of the top and bottom 250px that Instagram’s story UI covers.
- **Export safety.** I tested glyph coverage in the kit fonts: arrows, ≠, ✓ and ≤ are missing, so every check, cross, arrow and plus sign is inline SVG. All numbers are literal text. I confirmed that `text-wrap: balance` and `pretty` survive the export. I also found that exported text sets slightly narrower than the live page while box heights keep the live layout. That left a blank line in the slide 6 table, so I widened the answer column and checked every export again.

## Examples I tested before using them

- **Clinic.** “Staff cannot meet demand” is supported by the long waits and supports hiring. Hiring does not support the shortage. So the first sentence is the main conclusion.
- **Museum and forest.** Both apply a rule about every member of a group to one member. Both are valid, and they share the same structure.
- **Deck.** “Must have a permit to pass” makes the permit necessary. The conclusion treats it as sufficient.
- **Chess club** (“Most members are seniors. Jordan is a member.”):
  - “At least one member is a senior” must be true.
  - “Jordan is a senior” is supported but can be false.
  - “Jordan joined this year” is never discussed.
  - “No member is a senior” contradicts the facts.
- **Matrix** (net change = added maintenance minus $4,000; the conclusion holds exactly when added maintenance is under $4,000):
  - “Less than $4,000” strengthens, is sufficient and is necessary.
  - “No more than $1,000” strengthens and is sufficient. It is not necessary, because $3,000 still saves $1,000.
  - “Three comparable libraries had increases under $1,000” strengthens. It is not sufficient, because this library could differ. It is not necessary, because the argument never relies on other libraries.
