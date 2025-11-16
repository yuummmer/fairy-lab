# ✨ FAIRy Skeleton (demo runner)✨
# FAIRy Lab

> Repo name: `fairy-skeleton` • Web + CLI demo runner for [FAIRy Core](https://github.com/yuummmer/fairy-core)

FAIRy Lab is the self-hosted demo environment for **FAIRy** — a local-first validator and packager for FAIR-friendly, repository-ready datasets.

This repo gives you:

- A small CLI demo runner (`fairy-skel`) that calls the real engine in **FAIRy Core**
- Toy datasets and configs that show PASS / WARN / FAIL workflows
- Example outputs you can use in demos, talks, and screenshots
- (Experimental) a Streamlit app entry point (`app.py`) for a lightweight web UI

**FAIRy Lab is about workflows and demos.**  
**FAIRy Core is where the validator engine and rulepacks live.**

---

## What FAIRy Lab is / isn’t

**FAIRy Lab _is_:**

- A reference, self-hosted “lab” for exploring FAIRy:
  - Upload / point at sample TSVs
  - Run rulepacks via `fairy-skel`
  - Inspect findings, PASS/WARN/FAIL, and reports
- A place to keep:
  - Demo configs
  - Toy datasets
  - Example outputs (for screenshots, grants, and onboarding)

**FAIRy Lab _is not_:**

- The validator engine (that’s **FAIRy Core**)
- A multi-tenant hosted service (that would be a future “FAIRy Preflight+ / Teams” product)

All actual validation logic, rulepacks, and the `fairy` CLI live in  
👉 **[FAIRy Core](https://github.com/yuummmer/fairy-core)**

---

## TL;DR (quick start)

Assuming `fairy-core` and `fairy-skeleton` are siblings:

```bash
# 1) Create a virtualenv
python -m venv .venv
source .venv/bin/activate

# 2) Install FAIRy Core (engine)
cd ../fairy-core
pip install -e .

# 3) Install FAIRy Lab (this repo)
cd ../fairy-skeleton
pip install -e .

# 4) List and run demos
fairy-skel demos
fairy-skel run bulk_rnaseq_min     # intentionally FAILS (shows findings)
fairy-skel run bulk_rnaseq_pass    # clean PASS

```
Outputs are written to each demo’s out/ path defined in its config.yaml.
---
## Requirements
- Python 3.10+ (FAIRy-core polyfills datetime.UTC for 3.10)
- Unix-like shell (Linux/macOS/WSL)
-pip and venv (or conda/mamba equivalent)

---
## Getting Started
1. Clone both repos side-by-side (recommended layout):
projects/
  fairy-core/
  fairy-skeleton/
2. Install:

```bash
cd projects/fairy-core
python -m venv .venv && source .venv/bin/activate
pip install -e .

cd ../fairy-skeleton
pip install -e .

```
3. Run a demo:
```bash
fairy-skel demos
fairy-skel run bulk_rnaseq_min   # FAIL + WARN (shows findings)
fairy-skel run bulk_rnaseq_pass  # PASS (submission_ready: True)

```
Or call the engine directly
```bash
fairy preflight \
  --rulepack /absolute/path/to/fairy-core/src/fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json \
  --samples  /absolute/path/to/samples.tsv \
  --files    /absolute/path/to/files.tsv \
  --out      /path/to/out/report.json

```

## 🧪 Demos
Each demo is a folder under demos/<name> with a config.yaml:
```yaml
rulepack: /abs/path/to/fairy-core/src/fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json
inputs:
  samples: demos/<name>/inputs/samples.tsv
  files:   demos/<name>/inputs/files.tsv
out: demos/<name>/out/report.json
```
Current demos:
- bulk_rnaseq_min - intentionally FAIL + WARN to show findings
- bulk_rnaseq_pass - clean PASS

List all the demos:
```bash
fairy-skel demos
```
Run one:
```bash
fairy-skel run <name>
```
---
## 🗺️ Roadmap (v0.1 scope)
Streamlit Export & Validate tab wired to backend (warn-mode).

Deterministic report.json writer validated by JSON Schema.

Golden fixture test for bad.csv.

(See GitHub issues for v0.2 items like bundles, manifests, ZIP export, and provenance.)
---
## Create your own demo
```bash
mkdir -p demos/my_demo/inputs

# Provide TAB-separated TSVs
# samples.tsv
cat > demos/my_demo/inputs/samples.tsv <<'TSV'
sample_id	organism	collection_date
S1	Homo sapiens	2025-01-01
S2	Homo sapiens	2025-01-02
TSV

# files.tsv
cat > demos/my_demo/inputs/files.tsv <<'TSV'
sample_id	path
S1	reads/S1_R1.fastq.gz
S2	reads/S2_R1.fastq.gz
TSV

# config.yaml
cat > demos/my_demo/config.yaml <<'YAML'
rulepack: /absolute/path/to/fairy-core/src/fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json
inputs:
  samples: demos/my_demo/inputs/samples.tsv
  files:   demos/my_demo/inputs/files.tsv
out: demos/my_demo/out/report.json
YAML

# Try it
fairy-skel run my_demo

```
Tip: you can also point inputs: to files inside fairy-core/demos/... via absolute paths or symlinks.
---
## Repo structure & legacy note
- fairy_skeleton/ — small demo runner CLI (fairy-skel)
- demos/ — demo configs + inputs + outputs
- scripts/run_demo.sh — helper invoked by the runner
- _legacy/ — archived code moved out of the package; not shipped.
We prefer our branch during merges for this folder via .gitattributes.

Packaging: only fairy_skeleton* is packaged. The validator engine lives in FAIRy-core.
---
## FAIRy-core + versions
- Engine repo: https://github.com/yuummmer/fairy-core
- CLI commands available there: fairy validate, fairy preflight
- This skeleton requires FAIRy-core ≥ 0.1.0

(Coming soon: a tiny matrix mapping skeleton tags → minimum core version.)
---
## Development & tests
Skeleton has a minimal test/smoke setup. Most tests live in FAIRy-core.
```bash
pytest -q
```
Optional GitHub Actions “smoke” workflow suggestion:

- run pip install -e . (core + skeleton)
- fairy-skel run bulk_rnaseq_min and assert an output file exists
---
## Issues & support
- Engine/validator bugs → FAIRy-core issues
- Demo runner or example configs here → this repo’s issues

Security reports should target FAIRy-core.
---
## 📜 License

This repository (“FAIRy Lab” / FAIRy-skeleton) is licensed under a primarily permissive license:

- **Application / UI code in this repo** (e.g. `src/**`, front-end / API glue):  
  Licensed under **MIT**. See [`LICENSE`](./LICENSE).

- **Example rulepacks, lab configs, and workflows** (if present, e.g. under `labs/**` or `rulepacks/**`):  
  Intended to be **maximally reusable**. By default these follow the license
  of this repo (MIT), but we may mark some directories or files as
  **CC0-1.0** via a local `LICENSE` file if they’re meant as public-domain
  building blocks.

- **Example datasets, notebooks, and documentation assets** (e.g. `examples/**`, `data/**`, `notebooks/**`):  
  Unless otherwise noted, these are provided under **CC BY-4.0** so they can
  be reused with attribution. If a folder has its own `LICENSE` file, that
  file takes precedence for that content.

- **Third-party components**:  
  See [`THIRD_PARTY_LICENSES.md`](./THIRD_PARTY_LICENSES.md) if present.

The underlying engine, **FAIRy-core**, is licensed under **AGPL-3.0-only**  
(see the core repository for details). If you embed or call FAIRy-core as part
of a product or service, the AGPL terms for FAIRy-core still apply unless you
have a separate commercial license for the core. For commercial licensing
questions around FAIRy-core, contact **hello@datadabra.com**.
---

## 📸 Screenshot

### Dashboard view
![FAIRy Dashboard](FAIRy_Dash.png)
---

## Citation

If you use FAIRy in demos or talks, please cite:

FAIRy (v0.1). Local-first validator for FAIR data.
FAIRy-core: https://github.com/yuummmer/fairy-core
FAIRy Lab: https://github.com/yuummmer/fairy-skeleton
