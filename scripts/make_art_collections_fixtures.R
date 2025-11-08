library(tidytuesdayR)
library(dplyr)
library(readr)
library(fs)
library(here)

set.seed(42)

# Load TidyTuesday (Art Collections – 2021-01-12)
tuesdata <- tidytuesdayR::tt_load("2021-01-12")
artworks_raw <- if ("artwork" %in% names(tuesdata)) tuesdata$artwork else tuesdata$artworks
artists_raw  <- tuesdata$artists

# Minimal columns
art_cols    <- c("id", "artistId", "title", "acquisitionYear", "url", "medium")
artist_cols <- c("id", "name")

# Artworks: select + sanity
artworks_min <- artworks_raw %>%
  select(any_of(art_cols)) %>%
  filter(!is.na(id), !is.na(artistId))

# Artists: rename id -> artistId for FK match
artists_min <- artists_raw %>%
  select(any_of(artist_cols)) %>%
  transmute(artistId = id, artist = name)

# Sample a small, reproducible subset
n_take <- min(50, nrow(artworks_min))
artworks_sml <- artworks_min %>% slice_sample(n = n_take)

# Keep only referenced artists
artists_sml <- artists_min %>%
  semi_join(artworks_sml %>% distinct(artistId), by = "artistId")

# Write into repo (relative to repo root)
outdir <- here("katas", "art-collections", "fixtures")
dir_create(outdir)
write_csv(artworks_sml, file.path(outdir, "artworks.csv"))
write_csv(artists_sml,  file.path(outdir, "artists.csv"))

cat(
  "artworks rows:", nrow(artworks_sml),
  "\nartists rows:", nrow(artists_sml), "\n",
  "artworks path:", normalizePath(file.path(outdir, "artworks.csv")),
  "\nartists path:",  normalizePath(file.path(outdir, "artists.csv")), "\n"
)
