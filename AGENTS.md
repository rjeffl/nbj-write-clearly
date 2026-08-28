# Repository instructions

- Keep the skill's authority order, source-fidelity boundary, and audit-only boundary intact.
- Keep `SKILL.md` lean and route specialized technical guidance through its one-level reference.
- Do not copy passages from the Google guide into authored guidance (`SKILL.md`, `references/guide.md`, `references/anti-slop.md`). Paraphrase, link, and preserve attribution. The licensed, attributed snapshots under `references/official/` are a separate archival mechanism, generated only by `scripts/sync-official.ts` — never edit them by hand.
- `references/anti-slop.md` is authored guidance adapting MIT-licensed material from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop). Keep its attribution footer and the NOTICE.md entry in sync when editing it. It is not a synced snapshot; no update machinery exists or is planned.
- Treat the guide as house guidance rather than an objective rule set.
- Run `scripts/check.sh` after every change.
- Report package validation separately from real-world writing quality.
