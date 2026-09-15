#!/usr/bin/env python3
"""Tests for the skill's sentence_stats.py. Run with: python3 scripts/test_sentence_stats.py"""

import contextlib
import importlib.util
import io
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", ".agents", "skills", "nbj-write-clearly", "scripts", "sentence_stats.py")
spec = importlib.util.spec_from_file_location("sentence_stats", SCRIPT)
stats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats)

LONG = " ".join(["Word"] + ["word"] * 39) + "."

SAMPLE = f"""---
title: sample
---

# Heading one

This short sentence stays unflagged. {LONG}

The cache fills — the node restarts; the probe fails.

Run `a; b — c` with care, e.g. twice. The call returns.

- A list item is its own paragraph.
- **One** bold and **two** bold spans here.

The value is X, not Y, rather than Z, instead of W.

```
{LONG} this; code — is skipped.
```

| table | {LONG} |
|---|---|

<!--
{LONG}
-->

> Quoted prose counts too.

## Changelog

{LONG}
"""


class SentenceStatsTest(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".md")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(SAMPLE)

    def tearDown(self):
        os.remove(self.path)

    def run_analyze(self, exclude=()):
        return stats.analyze(self.path, 35, [stats.re.compile(e, stats.re.I) for e in exclude])

    def test_skips_code_tables_comments_front_matter(self):
        result = self.run_analyze(exclude=["changelog"])
        self.assertEqual(result["summary"]["over_max_words"], 1)

    def test_excluded_heading_section(self):
        self.assertEqual(self.run_analyze()["summary"]["over_max_words"], 2)
        self.assertEqual(self.run_analyze(exclude=["changelog"])["summary"]["over_max_words"], 1)

    def test_joins_ignore_code_spans_and_abbreviations(self):
        flagged = {s["text"][:9]: s for s in self.run_analyze(["changelog"])["sentences"]}
        self.assertEqual(flagged["The cache"]["joins"], 2)
        self.assertNotIn("Run `a; b", flagged)

    def test_counts(self):
        s = self.run_analyze(["changelog"])["summary"]
        self.assertEqual(s["sentences"], 9)
        self.assertEqual(s["em_dashes"], 1)
        self.assertEqual(s["semicolons"], 1)
        self.assertEqual(s["paragraphs_over_two_contrasts"], 1)
        self.assertEqual(s["paragraphs_over_one_bold"], 1)

    def test_line_numbers(self):
        flagged = self.run_analyze(["changelog"])["sentences"]
        self.assertEqual([x["line"] for x in flagged], [7, 9])

    def test_cli_exit_codes(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(stats.main([self.path, "--json"]), 0)
            self.assertEqual(stats.main([self.path + ".missing"]), 2)


if __name__ == "__main__":
    unittest.main()
