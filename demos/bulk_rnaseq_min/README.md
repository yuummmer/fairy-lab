# Bulk RNA-seq (minimal, intentionally failing)

- Rulepack: GEO-SEQ-BULK v0.1.0
- Inputs: 2 samples / 3 files (mismatch to trigger `CORE.ID.UNMATCHED_SAMPLE`)
- How to run:
  ```bash
  fairy-skel run bulk_rnaseq_min
  # Output: demos/bulk_rnaseq_min/out/report.json

## Add a “passing” demo too (so folks can see green)
```bash
mkdir -p demos/bulk_rnaseq_pass/inputs

# reuse scratchrun but fix the mismatch (make files line up to S1,S2 only)
cat > demos/bulk_rnaseq_pass/inputs/samples.tsv <<'TSV'
sample_id       organism        collection_date
S1      Homo sapiens    2025-01-01
S2      Homo sapiens    2025-01-02
TSV

cat > demos/bulk_rnaseq_pass/inputs/files.tsv <<'TSV'
sample_id       path
S1      reads/S1_R1.fastq.gz
S2      reads/S2_R1.fastq.gz
TSV

cat > demos/bulk_rnaseq_pass/config.yaml <<'YAML'
rulepack: /home/jenni/projects/fairy-core/src/fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json
inputs:
  samples: demos/bulk_rnaseq_pass/inputs/samples.tsv
  files:   demos/bulk_rnaseq_pass/inputs/files.tsv
out: demos/bulk_rnaseq_pass/out/report.json
YAML
```
```bash
# try it
fairy-skel demos
fairy-skel run bulk_rnaseq_pass
```
You should see:

- submission_ready: True
- FAIL findings: 0 []
- WARN findings: 0 []
- demos/bulk_rnaseq_pass/out/report.json written.

If you still get a WARN:

- Make sure your files are TAB-separated (those <<'TSV' blocks above include real tabs).
- Ensure dates are valid ISO-8601 (e.g., 2025-01-02, not 2025-02-30).
