# Kata: Art Collections (TidyTuesday 2021-01-12)

## Goal
Practice a specimen-like rulepack with referential integrity + basic policy checks.

## Files
- `fixtures/artworks.csv` (id, artistId, title, acquisitionYear, url, medium)
- `fixtures/artists.csv`  (artistId, artist)

## Checks to implement (5–7)
- **required-columns (artworks)**: id, artistId, title, acquisitionYear, url
- **required-columns (artists)**: artistId, artist
- **id-unique (artworks)**: `id` has no duplicates
- **artist-foreign-key**: every `artworks.artistId` exists in `artists.artistId`
- **year-range**: `acquisitionYear` numeric + within [min_year, max_year]
- **url-format**: `url` is valid http(s)
- **title-trimmed** (optional warn): non-empty after trim
- **medium-policy** (optional warn): flag if `medium` contains any tokens in `medium_policy`

## Parameters (tune during practice)
```yaml
min_year: 1600
max_year: 2025
medium_policy: ["unknown", "photograph"]  # example only; tweak
```
## Done when
- Rulepack runs locally and produces a report
- At least 1 structural, 1 semantic, 1 policy check implemented
- Golden report comparison passes (expected/report.json)