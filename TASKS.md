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
- [ ] Consider spelling out a lighter-weight path in SKILL.md for short artifacts (one-line commit messages, brief review comments) — the full 12-step workflow (11 steps before `cohesion.md` was added on 2026-09-15) and validation checklist (10 points as of 2026-08-28) are heavy for those.
- [ ] `references/anti-slop.md` was adapted 2026-08-28 from petergyang/no-ai-slop upstream main; no sync is planned. Revisit only if upstream adds materially new patterns.
- [ ] From review (2026-08-28): consider two `check.sh` greps guarding the anti-slop attribution (footer present in `references/anti-slop.md`, entry present in `NOTICE.md`), mirroring the snapshot-header check.
- [ ] From review (2026-08-28): consider reproducing the full MIT permission notice under the no-ai-slop heading in `NOTICE.md`; naming the license and copyright holder is the current middle ground.
- [ ] From review (2026-08-28): the audit report format is stated in both `SKILL.md` (Protect meaning and voice) and `references/anti-slop.md` (Report format for audits); watch for drift if either changes.
- [x] Forward test for `references/cohesion.md`: run 2026-09-15 and recorded in `EVALUATION.md`.
- [x] Forward test for `references/sentences.md` and `sentence_stats.py`: run 2026-09-15 on real excerpts and recorded in `EVALUATION.md`.
- [x] Re-test the split-without-adding-claims rule in `sentences.md`: run 2026-09-15 and recorded in `EVALUATION.md`. The original failure didn't recur; on a trap draft the rule made no measurable difference.
- [x] Widen the split rule to relationships and effects with non-test examples, and re-test with three runs per arm: done 2026-09-15 and recorded in `EVALUATION.md`. There was no harm and slightly less drift, but the difference is within noise.
- [x] `SKILL.md` step 4 ("Name the actor") led five of six runs to invent "we" for a passive decision record. Limit added and re-tested 2026-09-15 (`EVALUATION.md`): no run in either arm invented an actor, so the fix is harmless but unproven.
- [x] `sentences.md` "Measure long documents first": one run's relative script path failed. The command is now `SKILL_DIR/scripts/sentence_stats.py` with an instruction to use the absolute path; all six re-test runs' first calls succeeded in both arms.
- [ ] Four of six actor re-test runs merged two conflicting source statements (30-day trigger, 14-day window) into a timeline the source doesn't state, then flagged it. Rule added 2026-09-15 to `SKILL.md` "Protect meaning and voice" and its validation checklist; not yet forward-tested.
- [ ] Watch the sentence rules against `official/sentence-structure.md` after each `sync-official` run: `sentences.md` defers to that page's condition-before-instruction rule, and a change there may need a matching change here.
- [ ] Watch for overlap between `cohesion.md` and `anti-slop.md`: the section-ending rule restates the pre-announcement and summary-recap patterns, and connective padding sits close to the intensifier list.
