#!/usr/bin/env python3
"""Report sentence-structure signals in the prose of a Markdown file.

The script counts sentence length, joins (em dashes, semicolons, and ", which"),
contrasts, and bold spans. It then lists the sentences and paragraphs to review
against references/sentences.md. The numbers tell an agent where to look. They
don't decide whether a sentence needs to change.

Code blocks, tables, headings, HTML comments, and front matter are skipped.
Sentence splitting is heuristic, so treat every count as approximate.
"""

import argparse
import json
import re
import statistics
import sys

JOIN_RE = re.compile(r"—|\s--\s|;|,\s+which\b")
CONTRAST_RE = re.compile(r"\brather than\b|[,—]\s*not\b|\binstead of\b", re.I)
BOLD_RE = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")
LIST_RE = re.compile(r"^(?:[-*+]|\d+[.)])\s+")
QUOTE_RE = re.compile(r"^(?:>\s?)+")
RULE_RE = re.compile(r"^[-*_]{3,}$")
CODE_RE = re.compile(r"`[^`]*`")
LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")
ABBREV_RE = re.compile(r"\b(?:e\.g|i\.e|etc|vs|cf|approx)\.", re.I)
BOUNDARY_RE = re.compile(r"[.!?][\"')\]*_]*\s+(?=[\"'(\[*_`A-Z0-9§~])")
MIN_WORDS = 3


def mask(text):
    """Blank out spans whose punctuation must not split or count, keeping offsets."""
    text = CODE_RE.sub(lambda m: "X" * len(m.group()), text)
    text = LINK_TARGET_RE.sub(lambda m: "]" + "x" * (len(m.group()) - 1), text)
    return ABBREV_RE.sub(lambda m: m.group().replace(".", "x"), text)


def paragraphs(lines, exclude):
    """Yield prose paragraphs as lists of (line_number, text)."""
    paras, buf = [], []
    fence, in_comment, skip_level = None, False, None
    start = 0
    if lines and lines[0].strip() == "---":
        for n in range(1, len(lines)):
            if lines[n].strip() == "---":
                start = n + 1
                break

    def flush():
        if buf:
            paras.append(list(buf))
            buf.clear()

    for n in range(start, len(lines)):
        s = QUOTE_RE.sub("", lines[n].strip()).strip()
        if fence:
            if s.startswith(fence):
                fence = None
            continue
        if s.startswith("```") or s.startswith("~~~"):
            flush()
            fence = s[:3]
            continue
        if in_comment:
            in_comment = "-->" not in s
            continue
        if s.startswith("<!--"):
            flush()
            in_comment = "-->" not in s
            continue
        heading = HEADING_RE.match(s)
        if heading:
            flush()
            level = len(heading.group(1))
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if skip_level is None and any(r.search(heading.group(2)) for r in exclude):
                skip_level = level
            continue
        if skip_level is not None:
            continue
        if not s or s.startswith("|") or RULE_RE.match(s):
            flush()
            continue
        if LIST_RE.match(s):
            flush()
            s = LIST_RE.sub("", s, count=1)
        buf.append((n + 1, s))
    flush()
    return paras


def split_sentences(para):
    """Split one paragraph into (line_number, text, masked_text) sentences."""
    text, starts = "", []
    for line_number, s in para:
        if text:
            text += " "
        starts.append((len(text), line_number))
        text += s
    masked = mask(text)
    cuts = [m.end() for m in BOUNDARY_RE.finditer(masked)] + [len(text)]
    out, prev = [], 0
    for cut in cuts:
        seg = text[prev:cut].strip()
        if seg:
            line_number = max(ln for off, ln in starts if off <= prev)
            out.append((line_number, seg, masked[prev:cut]))
        prev = cut
    return out, text, masked


def analyze(path, max_words, exclude):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    sentences, flagged, para_flags = [], [], []
    em_dashes = semicolons = 0
    for para in paragraphs(lines, exclude):
        sents, text, masked = split_sentences(para)
        contrasts = len(CONTRAST_RE.findall(masked))
        bold = len(BOLD_RE.findall(text))
        em_dashes += masked.count("—")
        semicolons += masked.count(";")
        if contrasts > 2 or bold > 1:
            para_flags.append({"line": para[0][0], "contrasts": contrasts, "bold": bold})
        for line_number, seg, mseg in sents:
            words = len(re.sub(r"[*`]", "", seg).split())
            if words < MIN_WORDS:
                continue
            joins = len(JOIN_RE.findall(mseg))
            sentences.append(words)
            if words > max_words or joins >= 2:
                flagged.append({"line": line_number, "words": words, "joins": joins, "text": seg})
    n = len(sentences)
    ordered = sorted(sentences)
    summary = {
        "sentences": n,
        "median_words": statistics.median(ordered) if n else 0,
        "mean_words": round(statistics.mean(ordered), 1) if n else 0,
        "p90_words": ordered[int(n * 0.9)] if n else 0,
        "max_words": ordered[-1] if n else 0,
        "over_max_words": sum(w > max_words for w in ordered),
        "two_plus_joins": sum(1 for s in flagged if s["joins"] >= 2),
        "em_dashes": em_dashes,
        "semicolons": semicolons,
        "paragraphs_over_two_contrasts": sum(p["contrasts"] > 2 for p in para_flags),
        "paragraphs_over_one_bold": sum(p["bold"] > 1 for p in para_flags),
    }
    return {"file": path, "max_words": max_words, "summary": summary,
            "sentences": flagged, "paragraphs": para_flags}


def print_report(result, limit):
    s = result["summary"]
    n = s["sentences"] or 1
    print(result["file"])
    print(f"  sentences {s['sentences']} | words median {s['median_words']}, "
          f"mean {s['mean_words']}, p90 {s['p90_words']}, max {s['max_words']}")
    print(f"  over {result['max_words']} words: {s['over_max_words']} "
          f"({100 * s['over_max_words'] // n}%) | 2+ joins: {s['two_plus_joins']} | "
          f"em dashes {s['em_dashes']} | semicolons {s['semicolons']}")
    print(f"  paragraphs with >2 contrasts: {s['paragraphs_over_two_contrasts']} | "
          f">1 bold span: {s['paragraphs_over_one_bold']}")
    items = [(x["line"], f"({x['words']} words, {x['joins']} joins) {x['text'][:110]}")
             for x in result["sentences"]]
    items += [(p["line"], f"paragraph: {p['contrasts']} contrasts, {p['bold']} bold spans")
              for p in result["paragraphs"]]
    items.sort()
    if items:
        print("  review:")
    for line_number, desc in items[:limit or None]:
        print(f"    L{line_number} {desc}")
    if limit and len(items) > limit:
        print(f"    ... {len(items) - limit} more; pass --limit 0 to list all")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("files", nargs="+")
    parser.add_argument("--max-words", type=int, default=35)
    parser.add_argument("--exclude-heading", action="append", default=[], metavar="REGEX",
                        help="skip sections whose heading matches; repeatable")
    parser.add_argument("--limit", type=int, default=40, help="review items to list; 0 for all")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    exclude = [re.compile(r, re.I) for r in args.exclude_heading]
    try:
        results = [analyze(f, args.max_words, exclude) for f in args.files]
    except OSError as err:
        print(f"sentence_stats: {err}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for result in results:
            print_report(result, args.limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
