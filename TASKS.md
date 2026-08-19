# Tasks

Non-blocking follow-ups from reviews (2026-08-19).

- [ ] Treat every `git pull upstream main` as a reviewable change: run a security review on `git diff <last-reviewed-tag>...upstream/main` before merging, since this content is injected into all Claude Code sessions.
- [ ] Reviewed upstream state is pinned as tag `reviewed-upstream-56e3a27`; move/add a new tag after each upstream review.
- [ ] If CI is added later: secrets scan over the repository.
- [x] Invisible-Unicode check for `.agents/skills/**`: automated by `scripts/sync-official.ts` for newly synced snapshot files. A repo-wide check for authored files would still belong in CI.
- [ ] Re-run `bun run sync-official` when [What's new](https://developers.google.com/style/whats-new) shows guide changes; review the resulting diff before merging.
- [ ] Optional: add own copyright line for fork modifications alongside the retained upstream MIT line if the fork is published more widely.
- [ ] Be aware the skill can trigger outbound fetches to developers.google.com for specialized rules ("when browsing is available") — legitimate, hardcoded domain, but visible in permission prompts.
- [ ] Consider spelling out a lighter-weight path in SKILL.md for short artifacts (one-line commit messages, brief review comments) — the full 11-step workflow and 9-point validation checklist are heavy for those.
