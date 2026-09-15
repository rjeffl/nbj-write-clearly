# Changelog

All notable changes to this fork are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The upstream project is unversioned, so this fork records changes under Unreleased instead of adopting a version scheme upstream does not have.

## [Unreleased]

### Added

- `references/sentences.md`: authored guidance on structure inside a sentence. It covers one claim per sentence, subject-verb proximity, sentence endings, literal relationships instead of equation metaphors, complete sentences in prose, citation placement, noun stacks, and ten named sentence findings for audits. It states how it relates to the vendored `official/sentence-structure.md`.
- `scripts/sentence_stats.py` inside the skill: a standard-library Python script that measures sentence length, joins, contrasts, and bold spans in Markdown prose and lists the sentences to review.
- `scripts/test_sentence_stats.py` at the repository root, run by `scripts/check.sh` along with required-file and routing checks for `sentences.md` and the script.
- `references/cohesion.md`: authored guidance on flow between sentences, paragraphs, and sections. It covers known-to-new ordering, unambiguous references, logical connectives, section handoffs, parallel section structure, consistent certainty phrasing, and seven named flow findings for audits.
- Required-file and SKILL.md-routing checks for `cohesion.md` in `scripts/check.sh`.
- `references/anti-slop.md`, adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT): banned stock words, named machine-writing patterns, concreteness tests, and an audit report format. Word lists and some examples are reproduced verbatim under the MIT terms; the rest is reworked for a developer-documentation register.
- Required-file and SKILL.md-routing checks for `anti-slop.md` in `scripts/check.sh`.
- Vendored snapshots of all 70 Google Developer Documentation Style Guide pages linked from `official-index.md`, under `references/official/` (snapshot 2026-08-19), so specialized lookups read exact local text instead of fetching live pages.
- `scripts/sync-official.ts` (Bun) to generate and refresh the snapshots, with boilerplate stripping and invisible-Unicode validation.
- Snapshot presence and attribution-header checks in `scripts/check.sh`.

### Changed

- Broadened the skill's trigger scope from documentation artifacts to all developer-facing prose: code review feedback, code comments and docstrings, commit messages, merge request descriptions, and CHANGELOG entries (`SKILL.md` description and Outcome section).
- Added a fork notice to `README.md`.
- `SKILL.md` step 8 now routes drafts, revisions, and audits longer than a couple of sentences through `references/anti-slop.md`; the audit rule adopts a name-the-pattern, quote-the-line, state-the-fix report format; the validation checklist gains a machine-writing-pattern check.
- `README.md` and `NOTICE.md` describe and attribute the no-ai-slop adaptation.
- `SKILL.md` gains step 10, which routes drafts, revisions, and audits with more than one paragraph through `references/cohesion.md`. Former steps 10 and 11 are now 11 and 12. The validation checklist gains a flow check.
- `README.md` names `rjeffl/nbj-write-clearly` as a fork of `bjornjohansen/nbj-write-clearly` and describes the cohesion reference.
- `SKILL.md` step 7 now states the one-claim, subject-verb, and sentence-ending rules, routes to `references/sentences.md`, and asks for `sentence_stats.py` counts before and after revising a document of more than about 500 words. The validation checklist gains a sentence check.
- `references/anti-slop.md`'s formatting pattern now allows at most one bold span per paragraph.
