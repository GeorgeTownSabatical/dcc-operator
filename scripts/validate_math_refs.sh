#!/usr/bin/env bash
set -euo pipefail

grep -q "Core Coherence Functional" MATH.md
grep -q "Blockchain Justification Rule" MATH.md
grep -q "QSO Fabric Extension" MATH.md
grep -q "MATH.md" AGENTS.md

while IFS= read -r path; do
  grep -q "Mathematical Authority" "$path" || {
    echo "missing math authority reference: $path" >&2
    exit 1
  }
done < <(find docs -name '*.md' -type f | sort)

while IFS= read -r path; do
  grep -q "BC > 1" "$path" || {
    echo "missing blockchain optionality rule: $path" >&2
    exit 1
  }
done < <(find docs/blockchain -name '*.md' -type f | sort)

while IFS= read -r path; do
  grep -q "temporary coherent sections" "$path" || {
    echo "missing QSO temporary-section rule: $path" >&2
    exit 1
  }
  grep -q "No self-materializing program" "$path" || {
    echo "missing QSO safety gate: $path" >&2
    exit 1
  }
done < <(find docs/qso -name '*.md' -type f | sort)

echo "math refs: ok"
