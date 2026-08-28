# Tasks

Non-blocking follow-ups from reviews (2026-08-19).

- [ ] Treat every `git pull upstream main` as a reviewable change: run a security review on `git diff <last-reviewed-tag>...upstream/main` before merging, since this content is injected into all Claude Code sessions.
- [ ] Reviewed upstream state is pinned as tag `reviewed-upstream-56e3a27`; move/add a new tag after each upstream review.
- [ ] If CI is added later: secrets scan over the repository.
- [x] Invisible-Unicode check for `.agents/skills/**`: validated at write time by `scripts/sync-official.ts` and on every `scripts/check.sh` run over all skill Markdown files.
- [ ] Re-run `bun run sync-official` when [What's new](https://developers.google.com/style/whats-new) shows guide changes; review the resulting diff before merging.
- [ ] Consider a fetch retry for transient failures in `sync-official.ts` (currently a flaky page forces a full re-run).
- [ ] Consider type-checking `scripts/sync-official.ts` (`bunx tsc --noEmit`) in `check.sh` if more TypeScript is added.
- [ ] Cosmetic: Material Icons ligature glyphs concatenate with the following word in a few snapshot prose lines (e.g. `ui-elements.md` "arrow_rightexpander arrow") — strip or space icon ligatures in `sync-official.ts` if it bothers readers.
- [ ] Optional: add own copyright line for fork modifications alongside the retained upstream MIT line if the fork is published more widely.
- [ ] Be aware the skill can trigger outbound fetches to developers.google.com for specialized rules ("when browsing is available") — legitimate, hardcoded domain, but visible in permission prompts.
- [ ] Consider spelling out a lighter-weight path in SKILL.md for short artifacts (one-line commit messages, brief review comments) — the full 11-step workflow and validation checklist (10 points as of 2026-08-28) are heavy for those.
- [ ] `references/anti-slop.md` was adapted 2026-08-28 from petergyang/no-ai-slop upstream main; no sync is planned. Revisit only if upstream adds materially new patterns.
- [ ] From review (2026-08-28): consider two `check.sh` greps guarding the anti-slop attribution (footer present in `references/anti-slop.md`, entry present in `NOTICE.md`), mirroring the snapshot-header check.
- [ ] From review (2026-08-28): consider reproducing the full MIT permission notice under the no-ai-slop heading in `NOTICE.md`; naming the license and copyright holder is the current middle ground.
- [ ] From review (2026-08-28): the audit report format is stated in both `SKILL.md` (Protect meaning and voice) and `references/anti-slop.md` (Report format for audits); watch for drift if either changes.
