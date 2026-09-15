# Sentence structure

Apply this reference to any draft, revision, or audit longer than a couple of sentences. It governs what happens inside a statement: how many claims one sentence carries, where its subject and verb sit, and where it ends. cohesion.md governs how sentences connect to each other.

## How this relates to the official page

`references/official/sentence-structure.md` is the Google page with the same title. It covers one rule: put the circumstance, condition, or goal before an instruction. SKILL.md step 5 already applies that rule, and this file doesn't restate it.

When the two pull in different directions, the instruction rule wins. For example, "To delete the entire document, click **Delete**" delays its verb on purpose, and that's correct. The rules below apply to statements: sentences that describe, explain, or argue.

The official pages on semicolons, parentheses, and commas agree with this file. Read one only when a punctuation question isn't settled here.

## Measure long documents first

Sentence problems are easy to fix one at a time and easy to miss across a long document. For a document of more than about 500 words, run the bundled script before and after a revision:

```sh
python3 SKILL_DIR/scripts/sentence_stats.py FILE --exclude-heading changelog
```

Replace `SKILL_DIR` with the absolute path of the directory that contains `SKILL.md`. The working directory is usually the user's project, so a relative `scripts/` path fails. `--exclude-heading` skips sections that must not be revised, such as dated changelogs or quoted records. The script lists sentences over 35 words, sentences with two or more joins (an em dash, a semicolon, or ", which"), paragraphs with more than two contrasts, and paragraphs with more than one bold span.

The thresholds tell you where to look. They don't tell you what to change. A 40-word sentence that states one claim and ends in a short list can stand. Report the before and after counts with the revision, and revise a long document section by section rather than in one pass.

If the script can't run, read the three longest sentences in each section and apply the rules below to them.

## Give each sentence one claim

A claim is a statement that could be true or false on its own. A reason attached with *because* or *so* belongs to its claim and can share the sentence. A second claim, a consequence, or a caveat that could stand alone gets its own sentence.

Split instead of cutting. When the source argues a point, keep every reason and consequence, and give each one a sentence. The argument stays; only the packaging changes.

A split often needs a new subject, verb, or connective. Choose ones that say no more than the source did:

- **Labels.** Keep a label as a label, or turn it into a neutral lead-in. "SEC-4: tokens expire after an hour" becomes "Under SEC-4, tokens expire after an hour," not "SEC-4 is satisfied because tokens expire after an hour."
- **Modality.** Don't add *can*, *must*, or *will*, and don't turn *may* or *might* into *can*.
- **Relationships.** Link two facts with *because* or *so* only when the source states that one causes the other. "The index was rebuilt on Monday, and queries slowed that week" stays two facts. A possible explanation stays possible: "…which could explain the timeouts" becomes "That could explain the timeouts," not "That explains the timeouts."
- **Effects.** Keep a claim about what something does at the source's strength. "The linter is a safety net for typos" doesn't become "The linter catches typos," and "helps with" doesn't become "solves."

Not recommended:

> The retry timeout is 3 seconds rather than 1, because a full-size frame takes 1.1 seconds to send, and the value lives in the build configuration, never in the user settings — a device that boots with the wrong value needs a site visit.

Recommended:

> The retry timeout is 3 seconds, because a full-size frame takes 1.1 seconds to send. The value lives in the build configuration, not in the user settings. A device that boots with the wrong value needs a site visit to fix.

## Keep the subject next to its verb

- Don't put a parenthesis, a pair of dashes, or a long phrase between a subject and its main verb. Move the aside after the clause, or give it its own sentence.
- In a statement, put the main clause early. When a long qualification comes first, make it a separate sentence. Instructions are the exception: their condition comes first, as step 5 requires.

Not recommended: "The cache (which the proxy fills on the first request and clears every hour) serves stale data after a deploy."

Recommended: "The cache serves stale data after a deploy. The proxy fills it on the first request and clears it every hour."

## End the sentence where its claim ends

- When an em dash, a semicolon, ", which", or ", and" introduces a clause with a new subject or a new claim, end the sentence and start another.
- A semicolon can stay when the second clause continues the same claim, for example before *therefore* or *that is*.
- Make *which* refer to the noun directly before it. When *which* refers to a whole clause, name the thing instead: "…fails its checksum. That failure hides the real cause," not "…fails its checksum, which hides the real cause."

## State the relationship literally

- Replace a sentence that equates a situation with its consequence with the relationship itself. Write "A test run at reduced power must be repeated," not "A test run at reduced power is a test that has to be repeated."
- Where the author's voice depends on an aphorism, keep at most one per section, and put the literal statement next to it.
- Use a contrast such as *not Y*, *rather than Y*, or *instead of Y* only when the reader would otherwise assume Y. Otherwise state X alone. Several contrasts in one paragraph are a sign that the paragraph argues against things nobody claimed.

## Write complete sentences in prose

- Give every prose sentence a subject and a verb. Fragments are fine in tables, headings, captions, and labeled list items, but not in paragraphs.
- Repeat a verb instead of leaving it out. Write "The first fault sends two frames, and the second sends four," not "The first fault sends two frames, the second four."
- Turn a provenance note into a sentence with an actor. Write "The team found this during the first build, on 2026-09-14," not "Found during the first build, 2026-09-14."
- When a sentence must be reread to parse, reorder it. Typical causes are a phrase used as a noun ("is honored by when the handler runs") and an adjective placed after its noun ("the half provable on the bench").

## Put references at clause boundaries

- Place a citation, section number, or requirement identifier at the end of the clause it supports, or at the start of the sentence. Don't put it between a subject and its verb.
- A parenthesis that contains a clause of its own becomes a separate sentence.

## Unpack noun stacks

- When more than three nouns or hyphenated modifiers run together, unpack them with a preposition or a relative clause. Write "the rule that an event is never retained," not "the never-retain-an-event rule."
- Defined terms, identifiers, and product names are exempt. Keep them exactly as the source writes them.

## Sentence findings for audits

Report sentence problems in the audit format from anti-slop.md: pattern name, quoted line, fix. When the script ran, give its counts first.

- **Stacked claims.** One sentence carries two or more claims that could stand alone. Split them.
- **Trailing tail.** A dash, semicolon, ", which", or ", and" adds a clause with a new subject. End the sentence before it.
- **Clause-level which.** *Which* refers to a whole clause. Name the referent.
- **Split subject.** An aside separates a subject from its verb. Move the aside.
- **Equation metaphor.** "X is Y" stands in for cause and effect. State the relationship.
- **Contrast habit.** A contrast answers something nobody assumed, or several contrasts share a paragraph. State the positive claim.
- **Prose fragment.** A paragraph sentence lacks a subject or verb, or leaves out a repeated verb. Complete it.
- **Garden path.** The sentence must be reread to parse. Reorder it.
- **Buried citation.** A reference interrupts the clause it supports. Move it to a boundary.
- **Noun stack.** More than three nouns or modifiers run together. Unpack them.
