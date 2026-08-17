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
