#!/usr/bin/env bash
set -euo pipefail

# --- Config (override by exporting env vars before running) ---
RULEPACK="${RULEPACK:-/home/jenni/projects/fairy-core/src/fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json}"
SAMPLES="${SAMPLES:-/home/jenni/projects/fairy-core/demos/scratchrun/samples.tsv}"
FILES="${FILES:-/home/jenni/projects/fairy-core/demos/scratchrun/files.tsv}"
OUT="${OUT:-out/report.json}"

# --- Resolve runner (prefer 'fairy' from venv, fall back to module) ---
if command -v fairy >/dev/null 2>&1; then
  RUNNER=(fairy)
else
  RUNNER=(python -m fairy.cli.run)
fi

# --- Sanity checks ---
[ -f "$RULEPACK" ] || { echo "Missing RULEPACK: $RULEPACK"; exit 2; }
[ -f "$SAMPLES"  ] || { echo "Missing SAMPLES:  $SAMPLES";  exit 2; }
[ -f "$FILES"    ] || { echo "Missing FILES:    $FILES";    exit 2; }

mkdir -p "$(dirname "$OUT")"

# --- Run ---
"${RUNNER[@]}" preflight \
  --rulepack "$RULEPACK" \
  --samples  "$SAMPLES" \
  --files    "$FILES" \
  --out      "$OUT" || true

echo "Wrote $OUT"
