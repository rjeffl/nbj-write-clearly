# Changelog

All notable changes to this fork are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The upstream project is unversioned, so this fork records changes under Unreleased instead of adopting a version scheme upstream does not have.

## [Unreleased]

### Added

- `references/anti-slop.md`, adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT): banned stock words, named machine-writing patterns, concreteness tests, and an audit report format, reworked for a developer-documentation register.
- Required-file and SKILL.md-routing checks for `anti-slop.md` in `scripts/check.sh`.
- Vendored snapshots of all 70 Google Developer Documentation Style Guide pages linked from `official-index.md`, under `references/official/` (snapshot 2026-08-19), so specialized lookups read exact local text instead of fetching live pages.
- `scripts/sync-official.ts` (Bun) to generate and refresh the snapshots, with boilerplate stripping and invisible-Unicode validation.
- Snapshot presence and attribution-header checks in `scripts/check.sh`.

### Changed

- Broadened the skill's trigger scope from documentation artifacts to all developer-facing prose: code review feedback, code comments and docstrings, commit messages, merge request descriptions, and CHANGELOG entries (`SKILL.md` description and Outcome section).
- Added a fork notice to `README.md`.
- `SKILL.md` step 8 now routes drafts, revisions, and audits longer than a couple of sentences through `references/anti-slop.md`; the audit rule adopts a name-the-pattern, quote-the-line, state-the-fix report format; the validation checklist gains a machine-writing-pattern check.
- `README.md` and `NOTICE.md` describe and attribute the no-ai-slop adaptation.
