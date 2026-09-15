# Candidate comparison

Two skills were built from the same Chrome review of all 70 live guide pages:

1. A `skill-creator` candidate with a lean core, conditional technical reference, UI metadata, validation, and explicit authority and stopping rules.
2. A `write-a-skill` candidate with the main guidance and examples in one file under 100 lines.

Each candidate handled the same three requests in a fresh agent context: revise a release note while preserving factual limits, turn raw UI and command notes into a procedure, and audit risky prose without rewriting it. A third fresh agent compared the anonymous outputs.

## Blind result

| Category | `skill-creator` candidate | `write-a-skill` candidate |
|---|---:|---:|
| Meaning fidelity and instruction compliance | 29/30 | 30/30 |
| Clarity and naturalness | 20/20 | 19/20 |
| Reader- and task-first structure | 15/15 | 13/15 |
| Technical formatting and scanability | 15/15 | 14/15 |
| Claim discipline and source risk | 10/10 | 10/10 |
| Audit prioritization and usefulness | 9/10 | 10/10 |
| **Total** | **98/100** | **96/100** |

The `skill-creator` candidate won by a small margin. Its release-note paragraphing, procedure heading, code block, and labeled audit findings made the results easier to scan. The single-file candidate was slightly more faithful to one source phrase and slightly stronger in one audit-order judgment.

The published skill adds a targeted rule to preserve source modality such as *can*, *might*, *should*, and *will*. That change responds to the winner's only observed fidelity loss. The final package was structurally revalidated after the change, but the 98–96 comparison was not rescored.

This was a focused forward test, not a broad benchmark. Both candidates performed well, and the scores should be read as evidence for this packaging decision rather than a general claim about authoring frameworks.

# Anti-slop forward test (2026-08-28)

After `references/anti-slop.md` was added (adapted from petergyang/no-ai-slop, MIT), three fresh agent contexts each read `SKILL.md` and followed its workflow on scratch inputs outside the repository:

1. **Revise:** a ~180-word fake README introduction seeded with 16 tagged instances across the catalog: a throat-clearing opener, a portability-test filler sentence (containing one of five banned words), four further banned words, one em-dash cluster (three dashes, counted once), a binary contrast, importance puffery, a trailing *-ing* analysis, an empty phrase, weasel attribution, a colon reveal, a negative listing, a summary-recap ending, and a fake-profound kicker. Four technical tokens had to survive.
2. **Audit:** the same draft, audit-only.
3. **Control:** a clean, conforming runbook procedure, to test the stop rule.

## Result

| Check | Revise | Audit | Control |
|---|---|---|---|
| Read anti-slop.md via step 8 routing | yes | yes | yes |
| Seeded instances addressed | 16/16 | 16/16 found | n/a |
| Protected tokens intact | 4/4 | flagged as must-preserve | 4/4 |
| Name-pattern, quote-line, state-fix format | n/a | yes, ordered by impact | n/a |
| No machine-authorship claim | n/a | explicit disclaimer | n/a |
| Weasel claim cut or flagged, not sourced by invention | cut and flagged to author | flagged | n/a |
| Stop rule held (no over-editing) | n/a | no rewrite | one numeral-consistency fix, then stopped |

No pattern line needed sharpening after the runs. The audit run also caught two unseeded problems (announcement framing in the heading, an unanchored "the release" time reference), both from existing guide.md rules.

Like the candidate comparison above, this is evidence for this packaging decision, not a broad benchmark.

# Cohesion forward test (2026-09-15)

After `references/cohesion.md` was added, three fresh agent contexts each read `SKILL.md` and followed its workflow on scratch inputs outside the repository. The prompts asked for clarity and flow but didn't name `cohesion.md`, so the runs also tested the step 10 routing.

1. **Revise:** a ~300-word, eight-section operations document for a fictional edge cache, seeded with 14 tagged instances. The seeds were two broken chains, two synonym drifts, two orphan references, connective padding, a sentence cloned across three parallel sections, parallel sections in different shapes, compared facts not in a table, certainty drift, a missing relationship, a section pre-announcement, and a qualification separated into a Caveats section. Eight technical tokens and quantities had to survive.
2. **Audit:** the same draft, audit-only.
3. **Control:** a runbook written to follow the skill, with parallel sections, a comparison table, and consistent certainty, to test the stop rule.

## Result

| Check | Revise | Audit | Control |
|---|---|---|---|
| Read cohesion.md via step 10 routing | yes | yes | yes |
| Seeded instances addressed | 14/14 | 12/14 under the seeded pattern; 2 flagged under a neighboring rule | n/a |
| Protected tokens intact | 8/8 | n/a | all commands and file names |
| Missing facts flagged, not invented | 9 author questions; "Not stated" in table cells | fixes that need facts are routed to the author | n/a |
| Stop rule held (no over-editing) | n/a | no rewrite | two paragraphs moved, no wording changed |

Notes on the partial and borderline results:

- **Audit, two seeds under other names.** The missing relationship (`CACHE_REGION` unset, so the node exits) was reported as a condition placed after its instruction. The broken chain "Latency regressions trigger a rollback." was reported as a trigger with no threshold. Both lines were flagged with a usable fix.
- **Revise, certainty.** The status column kept three phrasings (*Live*, *Planned for October*, *Probably the first quarter*). These are three different levels of certainty, one phrasing each, so the result follows the rule. The seed was weaker than intended.
- **Revise, one small fidelity drift.** "the dashboard" became "the shared dashboard" even though the run listed the equivalence as a question for the author.
- **Control, not fully clean.** The control run moved the collector's timing warning above the restart step, which the existing condition-before-instruction rule requires. It then moved the gateway's note to keep both sections the same shape. It also flagged that "without an outage" conflicts with the collector's 5-second metrics gap. Both problems were authoring flaws in the control, not over-editing.

Unseeded problems caught: passive sentences with no actor (who drains and retries), dates without a year, an opening that doesn't say what is rolling out, and a sequence error in the seed itself (a node that exits and *then* reports an error).

One routing change followed. `cohesion.md` told the agent to read two `references/official/` pages, but no `SKILL.md` step routes there. One run read one of them, and two skipped both as unrouted. The pointers are now conditional: read a page only when the reference's own rules don't settle the question. That wording change was not re-tested.

Like the tests above, this is evidence for this packaging decision, not a broad benchmark.

# Sentence structure forward test (2026-09-15)

After `references/sentences.md` and `scripts/sentence_stats.py` were added, three fresh agent contexts each read `SKILL.md` and followed its workflow. The prompts asked for clarity and readability and named neither the reference nor the script.

Unlike the earlier tests, the revise and audit input was real text rather than seeded prose: 1,449 words from an implementation plan the skill had already revised once, taken from three sections that argue a point. Before the test, a reviewer listed nine known sentence patterns in it: stacked claims, trailing tails, equation metaphors, split subjects, buried citations, a garden path, contrast habit, prose fragments, and a noun stack.

1. **Revise:** revise the excerpt, keeping the project's argumentative voice, every identifier, and every hedge.
2. **Audit:** audit the same excerpt without rewriting it.
3. **Control:** a 188-word section written to follow the rules.

## Result

| Check | Revise | Audit | Control |
|---|---|---|---|
| Read sentences.md via step 7 routing | yes | yes | yes |
| Ran `sentence_stats.py` when over 500 words | yes, before and after | yes, before | correctly skipped at 188 words |
| Known patterns addressed | 8 of 9 | 6 of 9 fully, 2 partly | n/a |
| Identifiers and numbers intact | all, checked by script | n/a | all |
| Stop rule held | n/a | no rewrite | one condition-first change from step 5 |

Script counts on the excerpt:

| Measure | Before | After revision |
|---|---|---|
| Sentences | 60 | 102 |
| Median / mean / p90 / max words | 19 / 23.5 / 44 / 60 | 14 / 14.4 / 21 / 37 |
| Over 35 words | 11 | 1, kept with a reason |
| Two or more joins | 5 | 0 |
| Em dashes / semicolons | 17 / 10 | 0 / 0 |
| Paragraphs with more than one bold span | 12 | 0 |

Notes:

- **Revise, the pattern not addressed.** "a single-frame frame" was kept. It's arguably a specification term, which the noun-stack rule exempts.
- **Revise, fidelity drift.** Splitting created sentences that needed new verbs, and two of those verbs added claims. A bare "R-5.3e:" label became "R-5.3e is met by a retained topic," and two new *can* sentences changed modality. The run flagged all three as questions for the author. `sentences.md` now says a split must not add a claim, certainty, or modality. That rule was not re-tested.
- **Audit, partial results.** A clause inside a parenthesis was reported as an orphan reference instead of a buried citation. Five contrasts were kept deliberately, each with a reason. The noun stack was not reported.
- **Unseeded finding with real consequence.** Both the revise and audit runs noticed that the excerpt calls the same module powers "tested" in one paragraph and "certified" in another, in a project whose rules forbid representing a node as certified.
- **Voice.** The revise run kept the source's British spellings and its lists without a serial comma as house style. The audit run recommended changing both. Project style outranks the skill, so the revise run's choice follows the authority order.

Like the tests above, this is evidence for this packaging decision, not a broad benchmark.

# Split-rule re-test (2026-09-15)

The sentence structure test above added one rule afterward: a verb that a split needs must add no claim, certainty, or modality. This test checked that rule in five fresh agent contexts. Each run revised a document with the skill and was not told what was under test.

## Design

- **A/B on a trap draft.** A 435-word set of engineering notes with 16 places where a natural split tempts an added claim: a bare requirement label, a status label, verbless fragments, *may* and *should* statements, a probable cause, a dash apposition, a recorded decision, and an efficacy metaphor. Two runs used the skill with the rule (A). Two used an identical copy without that one paragraph (B).
- **Regression on the original failure.** One A run revised the same real excerpt whose revision produced "R-5.3e is met by a retained topic" and two added *can*s. The rule's own example uses that label, so this run can confirm the fix but cannot show that the rule generalizes.

A script compared modal, hedge, and certainty word counts with the source. A reviewer then read every trap in every output.

## Result

| Check | A1 | A2 | B1 | B2 | Excerpt (A) |
|---|---|---|---|---|---|
| Modal and hedge counts match the source | yes | yes | yes | yes (one extra *would*, faithful) | yes |
| Added *can*, *must*, *will* or a compliance verb | none | none | none | none | none (the earlier run added three) |
| Label handling | "For REQ-12," | label kept | citation moved to clause end | label kept | "For R-5.3e," |
| Other drift | "catches" for "insurance against"; "That cause would explain" | an invented "so" linking a passing build to wrong transmit power | "catches" | "catches" | none found |
| Identifiers and numbers intact | yes | yes | yes | yes | yes |

## Reading the result

- **The original failure didn't recur.** The excerpt run wrote "For R-5.3e, `lran/bridge/version` carries…" and added no *can*. Because the rule quotes that case, this confirms the fix and nothing more.
- **On the trap draft, the rule made no measurable difference.** Neither arm added modality, a compliance claim, or certainty to a label. Baseline drift of that kind was already low without the rule.
- **The drift that remains is a different kind, and it appeared in both arms.** Runs replaced a hedged relationship with a stronger one: "cheap insurance against a regression" became "It catches a regression" in three of four runs. One run invented a causal *so*, and another turned "which would explain" into "That cause would explain." The rule's wording ("no claim") covers these in principle. Its example shows only a label and a modal verb.

With two runs per arm, a difference of one or two drift instances is noise. This is evidence about the rule's scope, not a benchmark.
