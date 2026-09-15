# Cohesion and flow

Apply this reference to any draft, revision, or audit with more than one paragraph. The rules in SKILL.md, guide.md, and anti-slop.md make each sentence clear on its own. This reference connects those sentences, so the reader follows one line of thought from start to finish without backtracking. The rules below are enough for most flow problems. When a pronoun or relative-clause question isn't settled by them, read `references/official/pronouns.md`. When a paragraph's length is in question, read `references/official/paragraph-structure.md`.

## Order each sentence from known to new

Start a sentence with something the reader already has: the subject of the previous sentence, a term just defined, or the topic the heading named. End it with the new information, where the next sentence can pick it up.

A sentence that opens on an unfamiliar term breaks the chain. Move the unfamiliar term to the end, or add the missing step that connects it.

Not recommended:

> The client retries a failed request after 2 seconds. A cached response is returned when the server sees a duplicate request ID. Request IDs are generated once per operation.

Recommended:

> The client retries a failed request after 2 seconds and sends the same request ID. Because the request ID is unchanged, the server recognizes the retry as a duplicate and returns its cached response.

## Refer back without ambiguity

- Repeat the exact term when more than one earlier noun could be the referent. Don't swap in a synonym for variety, because readers take a new word to mean a new thing.
- Follow *this*, *these*, *that*, and *such* with a noun: *this cache*, not *this*.
- Use *it* or *they* when exactly one earlier noun fits. Don't ban pronouns outright. A long noun phrase repeated in every sentence slows the reader down.

## Name the relationship between sentences

- When sentence order alone doesn't show how two sentences relate, state the relationship with a connective that carries logic: *because*, *so*, *but*, *instead*, *for example*, *as a result*, *after*, or *until*.
- When the order already makes the relationship clear, leave the connective out.
- Replace a chain of additive openers such as *Additionally*, *Furthermore*, *Moreover*, and *Also* with a list, or cut them. The chain signals parallel items written as prose.
- Short sentences don't have to read as disconnected. Join a short sentence to its neighbor when it only finishes the neighbor's thought. Split a long sentence when it carries two relationships.

## Hand off between paragraphs and sections

- Open each paragraph with a sentence that states its point or its relationship to the previous paragraph. Reading only the first sentence of each paragraph in a section should give a usable summary of that section.
- When the next section depends on something this section introduced, name it near the end of this section and reuse the same term at the start of the next.
- End a section on its last concrete point. Don't add a sentence that announces the next section or restates this one.
- Order content the way the reader uses it: prerequisites before steps, cause before effect, and the general case before exceptions.

## Give parallel sections a parallel shape

- When several sections describe items of the same kind, such as endpoints, sites, components, or configuration options, give each section the same subsections in the same order. The reader then finds the same fact in the same place every time.
- When readers compare the same facts across items, put those facts in one table instead of repeating them in each section.
- Repeat the structure, not the sentences. A sentence that appears word for word in several sections adds nothing after its first use. State it once, before the parallel sections, or cut it.
- When one item lacks a fact the others have, handle the gap the same way everywhere: write *None*, or omit the field in every section that lacks it.

## Keep certainty consistent

- Choose one phrasing for each level of certainty and use it throughout the document. For example, *is* for a fact, *is planned* for committed but unscheduled work, and *hasn't been decided* for an open question.
- Put a qualification next to the claim it qualifies, not in a later caveats section.
- Don't change the source's certainty to make the phrasing match. Preserve modality as SKILL.md requires.

## Flow findings for audits

Report flow problems in the audit format from anti-slop.md: pattern name, quoted line, fix.

- **Broken chain.** A sentence opens on a term the reader hasn't met. Reorder from known to new.
- **Synonym drift.** One concept has two names. Pick one.
- **Orphan reference.** *This*, *it*, or *they* has no single referent. Add the noun.
- **Missing relationship.** The reader must guess how two sentences connect. Add the logical connective.
- **Connective padding.** Additive openers stack across sentences. Use a list or cut them.
- **Cloned sentence.** The same sentence recurs across parallel sections. State it once.
- **Certainty drift.** One level of certainty has several phrasings, or a qualification is separated from its claim. Standardize and move it.
