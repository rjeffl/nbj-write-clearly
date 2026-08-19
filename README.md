# NBJ Write Clearly

> **Fork notice:** This is a fork of [daniel-p-green/nbj-write-clearly](https://github.com/daniel-p-green/nbj-write-clearly), adapted to trigger for all developer-facing output — code review feedback, code comments, commit messages, and merge request descriptions — not only documentation artifacts. See [CHANGELOG.md](CHANGELOG.md).

An unofficial agent skill for drafting, revising, and auditing clear technical and product documentation. It applies principles from the [Google Developer Documentation Style Guide](https://developers.google.com/style) while protecting facts, technical tokens, uncertainty, and the author's voice.

This is not a generic "simplify everything" prompt. It helps an agent decide what to preserve, what to change, which guidance applies to the destination, and when to stop editing.

## When to use it

Invoke `$nbj-write-clearly`, or let a compatible agent select it automatically, for:

- developer documentation and READMEs;
- procedures and help-center content;
- release notes and CHANGELOG entries;
- technical explanations;
- UI copy;
- code review feedback;
- code comments and docstrings; and
- commit messages and merge request descriptions.

Use it to draft new material, revise an existing draft, or audit prose without rewriting it. Do not treat it as a default voice layer for marketing, legal, academic, fictional, or personal writing unless you explicitly request this style.

## What it improves

- Leads with the reader's answer or goal.
- Names actors and puts conditions before instructions.
- Uses direct, globally understandable language without making every sentence sound the same.
- Structures procedures, code, UI references, links, lists, and headings for scanning.
- Removes unsupported claims, pre-announcements, jargon, filler, and vague AI-sounding language.
- Preserves facts, caveats, modal verbs, quotations, commands, filenames, API names, product names, and UI labels.

## Install

Clone the repository:

```sh
git clone https://github.com/bjornjohansen/nbj-write-clearly.git
cd nbj-write-clearly
```

To install the original, narrower-scope skill instead, clone the upstream repository: `https://github.com/daniel-p-green/nbj-write-clearly.git`.

Copy the skill into your agent's skill directory. For Codex:

```sh
mkdir -p ~/.codex/skills
cp -R .agents/skills/nbj-write-clearly ~/.codex/skills/
```

For agents that use `~/.agents/skills`:

```sh
mkdir -p ~/.agents/skills
cp -R .agents/skills/nbj-write-clearly ~/.agents/skills/
```

Start a new task so the agent refreshes its skill inventory.

## Use

Invoke the skill by name:

```text
Use $nbj-write-clearly to revise this draft for clarity without changing its facts or voice.
```

It can also audit without rewriting:

```text
Use $nbj-write-clearly to audit this procedure. Report the highest-risk clarity problems, but don't rewrite it.
```

The trigger description also lets compatible agents select the skill for any developer-facing prose: developer documentation, technical explanations, procedures, release notes, help-center content, UI copy, code review feedback, code comments, commit messages, and merge request descriptions.

## Design

The compact `SKILL.md` holds the core workflow, authority order, preservation rules, and completion check. A conditional reference adds high-frequency technical guidance for procedures, code, commands, UI, tables, images, accessibility, and detailed audits. A separate [official category index](.agents/skills/nbj-write-clearly/references/official-index.md) routes specialized compliance questions to the relevant live Google page without loading the whole guide for ordinary writing.

The source review inspected all 70 distinct content pages in the guide's live navigation on August 17, 2026. The skill deliberately operationalizes the core principles and high-frequency rules; it does not reproduce every word-list entry, punctuation exception, naming rule, or specialized format. For those cases, it routes the agent to the live guide. Project rules and reader clarity can still override house guidance when the result stays consistent.

See [EVALUATION.md](EVALUATION.md) for the candidate comparison and forward-test result.

## Inspiration and attribution

This project began with [an August 17, 2026 post by Nate B. Jones (@natebjones)](https://x.com/natebjones/status/2089457435459404093) suggesting that agents read the Google Developer Documentation Style Guide and turn it into a skill.

The skill paraphrases and reorganizes guidance from the [Google Developer Documentation Style Guide](https://developers.google.com/style). Google licenses its page content under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless otherwise noted and its code samples under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). This repository is unofficial and is not endorsed by Google.

## License

The original material in this repository is available under the [MIT License](LICENSE). Google's source material remains under its stated licenses. See [NOTICE.md](NOTICE.md) for details.
