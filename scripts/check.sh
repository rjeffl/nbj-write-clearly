#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_root="$repo_root/.agents/skills/nbj-write-clearly"

required_files=(
  "$repo_root/README.md"
  "$repo_root/LICENSE"
  "$repo_root/NOTICE.md"
  "$skill_root/SKILL.md"
  "$skill_root/agents/openai.yaml"
  "$skill_root/references/guide.md"
  "$skill_root/references/official-index.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

if ! grep -q '^name: nbj-write-clearly$' "$skill_root/SKILL.md"; then
  echo "SKILL.md has the wrong name." >&2
  exit 1
fi

if ! grep -q '^description: .*Use when' "$skill_root/SKILL.md"; then
  echo "SKILL.md description must explain when to use the skill." >&2
  exit 1
fi

if ! grep -q 'references/official-index.md' "$skill_root/SKILL.md"; then
  echo "SKILL.md must route specialized guidance to official-index.md." >&2
  exit 1
fi

skill_lines="$(wc -l < "$skill_root/SKILL.md")"
if (( skill_lines > 100 )); then
  echo "SKILL.md is $skill_lines lines; keep it at or below 100." >&2
  exit 1
fi

# references/official/ holds vendored Google pages that may legitimately
# contain TODO in code samples. sync-official.ts validates them for content
# length and invisible Unicode at write time; the checks below cover the rest.
if grep -R -n -E '/Users/|TODO|FIXME' \
  --exclude-dir=official \
  "$repo_root/README.md" \
  "$repo_root/EVALUATION.md" \
  "$repo_root/NOTICE.md" \
  "$repo_root/AGENTS.md" \
  "$skill_root"; then
  echo "Found a local path or unfinished placeholder." >&2
  exit 1
fi

official_dir="$skill_root/references/official"
official_count=$(find "$official_dir" -name '*.md' 2>/dev/null | wc -l)
if (( official_count < 1 )); then
  echo "No vendored snapshots in $official_dir; run scripts/sync-official.ts." >&2
  exit 1
fi
for file in "$official_dir"/*.md; do
  if ! head -2 "$file" | grep -q '^Source: https://developers\.google\.com/'; then
    echo "Missing snapshot header in $file." >&2
    exit 1
  fi
  # Literal markup examples must sit inside code fences; a bare HTML tag at
  # line start means the converter leaked an example into the document flow.
  if ! awk 'BEGIN { fence = 0 }
    /^ ? ? ?```/ { fence = !fence; next }
    !fence && /^<[a-zA-Z]/ { print FILENAME ":" FNR ": " $0; bad = 1 }
    END { exit bad }' "$file"; then
    echo "Raw HTML outside a code fence in $file." >&2
    exit 1
  fi
done

# Invisible or bidi Unicode anywhere in the skill is an injection vector.
if ! find "$skill_root" -name '*.md' -print0 | xargs -0 perl -CSD -ne '
  if (/[\x{200B}-\x{200F}\x{202A}-\x{202E}\x{2060}-\x{2064}\x{FEFF}\x{E0000}-\x{E007F}]/) {
    print STDERR "Invisible Unicode in $ARGV\n"; $found = 1;
  }
  END { exit 1 if $found }'; then
  exit 1
fi

if git -C "$repo_root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$repo_root" diff --check
fi

echo "All checks passed."
