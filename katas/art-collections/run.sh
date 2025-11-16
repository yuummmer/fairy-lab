#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")"/../.. && pwd)"

ART="$ROOT/katas/art-collections/fixtures/artworks.csv"
ARTISTS="$ROOT/katas/art-collections/fixtures/artists.csv"
JOINED="$ROOT/katas/art-collections/fixtures/artworks_joined.csv"
OUT="$ROOT/katas/art-collections/out.json"
RULES="$ROOT/katas/art-collections/rules/tate-art-collections@0.1.0.yaml"

python "$ROOT/scripts/prejoin_art_collections.py" "$ART" "$ARTISTS" "$JOINED"

fairy validate \
  --rulepack "$RULES" \
  --report-json "$OUT" \
  "$JOINED"
