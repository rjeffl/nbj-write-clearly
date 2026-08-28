# Machine-writing patterns

Apply this reference to any draft, revision, or audit longer than a couple of sentences. It removes stock words and patterns that read as generated filler. For punctuation and formatting mechanics such as dashes, colons, and bold, defer to [guide.md](guide.md) and the official pages listed in [official-index.md](official-index.md). Never change a listed word or pattern inside code, commands, quotations, API names, UI labels, or product names.

## Words to cut

Replace these stock words with the plain verb or the concrete mechanism, such as *use*, *help*, or what the thing actually does: delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, this is huge, this changes everything, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving.

Cut these intensifiers when they add nothing; keep one only when it carries real emphasis, uncertainty, or contrast: just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably. *Just* and *simply* also understate difficulty for the reader.

Cut these phrases; they delay the point: it's worth noting, it's important to note, at the end of the day, when it comes to, at its core, in today's world, the reality is, in order to, going forward, let's dive in.

## Patterns to cut

Each entry names the pattern, shows its shape, and gives the fix.

- **Binary contrast.** "It's not X. It's Y." State Y directly: "The eval matters more than the model."
- **Throat-clearing opener.** "Here's the thing," "Let me be clear." Delete it and state the point.
- **Faux-insight setup.** "What nobody tells you," "The part everyone misses." Cut the setup and let the claim stand on its own.
- **Colon reveal.** "The best part: it learns." Rewrite as a plain sentence. Colons that introduce lists, code blocks, and labels stay, per guide.md.
- **Superficial analysis.** A trailing *-ing* clause that pretends to explain: "adds file search, highlighting the team's commitment to better workflows." Replace it with the actual consequence: "adds file search, so users can find old drafts."
- **Importance puffery.** "Marks a pivotal moment," "plays a vital role," "stands as a testament." State the fact and let the reader judge: "The release is the project's first stable API."
- **Interpretive metadiscourse.** "The key takeaway is," "As you can see," "This distinction matters." If the point is already clear, delete the aside; otherwise add the missing fact instead.
- **Weasel attribution.** "Experts agree," "studies show," "widely regarded as." Name the source or cut the claim. If no source exists, ask the author instead of inventing one.
- **Fake-strong verb.** "Serves as a centralized hub for sponsor management." Prefer *is* and *has* when they are clearer: "tracks sponsors, drafts, and due dates in one place."
- **Negative listing.** "Not a wrapper. Not a plugin. A platform." Say what it is.
- **Dramatic fragmentation.** "Fast. Simple. Done." or "That's it. That's the release." Use complete sentences.
- **Rhetorical setup.** "What if I told you," "Think about it:", or a question the next sentence answers. Drop the setup and make the point.
- **Fake-profound kicker.** A closing metaphor or aphorism that restates the point as wisdom. Delete it and end on the last concrete point or next action. Do not write a better metaphor.
- **Summary-recap ending.** "In conclusion" followed by a restated paragraph. End on the last concrete point, takeaway, or next action. Keep a summary section when the destination requires one.
- **Formatting slop.** Emoji in headings, bold sprinkled mid-sentence for emphasis, a bullet list that reads better as two sentences of prose, or a heading over a two-sentence section. Bold UI labels required by guide.md are exempt.
- **Em-dash overuse.** Use no em dashes in short artifacts and at most one or two in a long draft, and only where they beat commas, periods, or parentheses. Format any kept dash per the dashes entry in [official-index.md](official-index.md).

## Concreteness tests

- **Portability test.** If a sentence could move unchanged into another project's documentation, it is filler. Cut it or anchor it with a fact, mechanism, consequence, or example specific to this subject.
- **Show, don't label.** Replace evaluative labels such as *powerful* or *seamless* with the measured behavior: "cut deploy time from 40 minutes to 4," not "significantly improves productivity."

## Report format for audits

When the task is an audit, report each finding as the pattern name, the quoted line, and the fix in a few words. Order findings by reader impact. Describe patterns, never provenance: do not claim or imply that a text is machine-written.

---

Adapted from [no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang (MIT License, Copyright (c) 2026 Peter Yang). The word lists and some examples are reproduced verbatim under those terms; the rest is reworked for a developer-documentation register. See NOTICE.md in this skill's source repository for details.
