# scripts/prejoin_art_collections.py
#!/usr/bin/env python
import sys, csv

art_path, artists_path, out_path = sys.argv[1:4]

# --- detect the key column in artists.csv ---
with open(artists_path, newline='', encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    header = [h.strip() for h in rdr.fieldnames or []]
    key_col = "artistId" if "artistId" in header else ("id" if "id" in header else None)
    if not key_col:
        raise SystemExit(f"Could not find artist id column in artists.csv; saw: {header}")
    artist_ids = { (row.get(key_col) or "").strip() for row in rdr if row.get(key_col) }

# --- annotate artworks with presence flag ---
with open(art_path, newline='', encoding='utf-8') as fin, \
     open(out_path, "w", newline='', encoding='utf-8') as fout:
    rdr = csv.DictReader(fin)
    fieldnames = list(rdr.fieldnames or []) + ["artist_exists"]
    w = csv.DictWriter(fout, fieldnames=fieldnames)
    w.writeheader()
    for row in rdr:
        aid = (row.get("artistId") or "").strip()
        row["artist_exists"] = "TRUE" if aid in artist_ids else "FALSE"
        w.writerow(row)

print(f"Wrote {out_path} with key_col={key_col} and {len(artist_ids)} artist ids")
