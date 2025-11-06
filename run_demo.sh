#!/usr/bin/env bash
set -euo pipefail
RULEPACK="/home/jenni/projects/fairy-core/src/fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json"
SAMPLES="/home/jenni/projects/fairy-core/demos/scratchrun/samples.tsv"
FILES="/home/jenni/projects/fairy-core/demos/scratchrun/files.tsv"
mkdir -p out
fairy preflight --rulepack "$RULEPACK" --samples "$SAMPLES" --files "$FILES" --out out/report.json || true
echo "Wrote out/report.json"