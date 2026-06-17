#!/usr/bin/env bash
set -euo pipefail

required_terms=(
  "state"
  "evidence"
  "provenance"
  "coherence score"
  "risk score"
  "repair path"
  "rollback path"
  "dissolution path"
)

agent_docs=(AGENTS.md)
while IFS= read -r path; do
  agent_docs+=("$path")
done < <(find docs/agents -name '*.md' -type f | sort)

for path in "${agent_docs[@]}"; do
  for term in "${required_terms[@]}"; do
    grep -qi "$term" "$path" || {
      echo "missing agent output term '$term' in $path" >&2
      exit 1
    }
  done
done

echo "agent contracts: ok"
