from pathlib import Path
import json
import zipfile

from fairy.core.services.export_adapter import export_submission
from fairy.cli.run import FAIRY_VERSION


HERE = Path(__file__).parent
GOLDEN = Path("tests/golden")
RULEPACK = Path("fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json")


def test_export_zip_smoke(tmp_path):
    """Happy-path export: produces a timestamped dir, report/manifest/provenance, and a non-empty ZIP."""
    project_dir = tmp_path / "proj"
    project_dir.mkdir(parents=True, exist_ok=True)

    samples = GOLDEN / "fixed" / "samples.tsv"
    files = GOLDEN / "fixed" / "files.tsv"
    assert samples.exists() and files.exists(), "Golden FIXED TSVs are missing"

    res = export_submission(
        project_dir=project_dir,
        rulepack=RULEPACK,
        samples=samples,
        files=files,
        fairy_version=FAIRY_VERSION,
    )

    # basics exist
    assert res.export_dir.exists()
    assert res.report_path.exists()
    assert res.report_md_path.exists()
    assert res.manifest_path.exists()
    assert res.provenance_path.exists()
    assert res.zip_path.exists() and res.zip_path.stat().st_size > 0

    # manifest has entries and sha256/bytes fields
    manifest = json.loads(res.manifest_path.read_text(encoding="utf-8"))
    assert isinstance(manifest, list) and len(manifest) >= 3
    for item in manifest:
        assert "path" in item and "sha256" in item and "bytes" in item

    # provenance carries minimal fields
    prov = json.loads(res.provenance_path.read_text(encoding="utf-8"))
    assert "created_at_utc" in prov
    assert prov.get("fairy_version") == FAIRY_VERSION

    # zip opens and contains the expected files
    with zipfile.ZipFile(res.zip_path, "r") as zf:
        names = set(zf.namelist())
        expected = {"samples.tsv", "files.tsv", "report", "report.md", "manifest.json", "provenance.json"}
        assert expected.issubset(names), f"ZIP missing files: {expected - names}"
        # ensure we didn't zip a zip inside itself
        assert "bundle.zip" not in names
