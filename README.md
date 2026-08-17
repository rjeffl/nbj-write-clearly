# NBJ Write Clearly

An unofficial agent skill inspired by [Nate B. Jones's post](https://x.com/natebjones/status/2089457435459404093) about turning the [Google Developer Documentation Style Guide](https://developers.google.com/style) into an AI writing skill. It turns the guide's most useful principles into a compact workflow for clear, natural technical and professional prose, with explicit safeguards for facts, technical tokens, uncertainty, and the author's voice.

This is not a generic "simplify everything" prompt. It helps an agent decide what to preserve, what to change, which guidance applies to the destination, and when to stop editing.

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
git clone https://github.com/daniel-p-green/nbj-write-clearly.git
cd nbj-write-clearly
```

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

The trigger description also lets compatible agents select the skill for documentation, explanations, procedures, release notes, UI copy, and related professional writing.

## Design

The 60-line `SKILL.md` holds the core workflow, authority order, preservation rules, and completion check. A conditional reference adds technical guidance only for procedures, code, commands, UI, tables, images, accessibility, and detailed audits. This keeps ordinary writing tasks lean without making technical behavior shallow.

The source review covered all 70 pages in the guide's live navigation on August 17, 2026. The skill keeps the guide's own philosophy: project rules and reader clarity can override house guidance when the result stays consistent.

See [EVALUATION.md](EVALUATION.md) for the candidate comparison and forward-test result.

## Inspiration and attribution

This project began with [an August 17, 2026 post by Nate B. Jones (@natebjones)](https://x.com/natebjones/status/2089457435459404093) suggesting that agents read the Google Developer Documentation Style Guide and turn it into a skill.

The skill paraphrases and reorganizes guidance from the [Google Developer Documentation Style Guide](https://developers.google.com/style). Google licenses its page content under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless otherwise noted and its code samples under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). This repository is unofficial and is not endorsed by Google.

## License

The original material in this repository is available under the [MIT License](LICENSE). Google's source material remains under its stated licenses. See [NOTICE.md](NOTICE.md) for details.
