import json
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
BAD_DIR = HERE / "bad"
FIXED_DIR = HERE / "fixed"
EXPECTED_DIR = HERE / "expected"
RULEPACK_PATH = Path("fairy/rulepacks/GEO-SEQ-BULK/v0_1_0.json")

def run_fairy(samples_path: Path, files_path: Path, out_dir: Path):
    """
    Run FAIRy on the given samples/files TSVs and write outputs into out_dir.
    The CLI will write:
      - out_dir/report        (JSON: attestation + findings)
      - out_dir/report.md     (Markdown one-pager)
    Return (CompletedProcess, out_dir).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    out_stem = out_dir / "report"

    result = subprocess.run(
        [
            "fairy",
            "preflight",
            "--rulepack", str(RULEPACK_PATH),
            "--samples", str(samples_path),
            "--files", str(files_path),
            "--out", str(out_stem),
        ],
        capture_output=True,
        text=True,
    )

    return result, out_dir

def load_json_file(p: Path):
    with open(p, "r") as f:
        return json.load(f)

def extract_codes(report_obj: dict):
    return {f.get("code") for f in report_obj.get("findings", [])}

def assert_no_fail_findings(report_obj: dict):
    for f in report_obj.get("findings", []):
        assert f.get("severity") != "FAIL", f"Unexpected FAIL in PASS run: {f}"

def normalize_report(raw: dict):
    """
    Strip volatile/run-specific stuff before comparing to the golden snapshot.
    We intentionally keep only the stable contract:
      - rulepack id/version, fairy version
      - submission_ready, fail_count, warn_count
      - findings[].code/severity/where/why/how_to_fix/details.kind/row/column
    We do NOT assert timestamps, file hashes, absolute paths, etc.
    """
    att = raw.get("attestation", {})
    stable_att = {
        "rulepack_id": att.get("rulepack_id"),
        "rulepack_version": att.get("rulepack_version"),
        "fairy_version": att.get("fairy_version"),
        "submission_ready": att.get("submission_ready"),
        "fail_count": att.get("fail_count"),
        "warn_count": att.get("warn_count"),
    }

    stable_findings = []
    for f in raw.get("findings", []):
        d = f.get("details", {})
        stable_findings.append({
            "code": f.get("code"),
            "severity": f.get("severity"),
            "where": f.get("where"),
            "why": f.get("why"),
            "how_to_fix": f.get("how_to_fix"),
            "details": {
                "kind": d.get("kind"),
                "row": d.get("row"),
                "column": d.get("column"),
            }
        })

    return {
        "attestation": stable_att,
        "findings": stable_findings,
    }

def test_fail_then_pass(tmp_path):
    #
    # FAIL RUN
    #
    fail_out_dir = tmp_path / "fail_out"
    res_fail, _ = run_fairy(
        BAD_DIR / "samples.tsv",
        BAD_DIR / "files.tsv",
        fail_out_dir,
    )

    # CLI should exit non-zero since submission_ready == False
    assert res_fail.returncode != 0, (
        f"Expected nonzero exit for FAIL run, got {res_fail.returncode}\n"
        f"STDERR:\n{res_fail.stderr}"
    )

    report_fail = load_json_file(fail_out_dir / "report")

    # submission_ready should be False and we should have at least one FAIL
    assert report_fail["attestation"]["submission_ready"] is False
    assert report_fail["attestation"]["fail_count"] > 0

    fail_codes = extract_codes(report_fail)
    assert "CORE.ID.UNMATCHED_SAMPLE" in fail_codes
    assert "CORE.DATE.INVALID_ISO8601" in fail_codes

    # Golden snapshot compare:
    golden_fail = load_json_file(EXPECTED_DIR / "report_bad.json")
    assert normalize_report(report_fail) == normalize_report(golden_fail), (
        "FAIL report no longer matches golden contract. "
        "If this was an intentional change to core behavior, "
        "update tests/golden/expected/report_bad.json."
    )

    #
    # PASS RUN
    #
    pass_out_dir = tmp_path / "pass_out"
    res_pass, _ = run_fairy(
        FIXED_DIR / "samples.tsv",
        FIXED_DIR / "files.tsv",
        pass_out_dir,
    )

    # CLI should exit 0 now
    assert res_pass.returncode == 0, (
        f"Expected exit code 0 for PASS run, got {res_pass.returncode}\n"
        f"STDERR:\n{res_pass.stderr}"
    )

    report_pass = load_json_file(pass_out_dir / "report")

    # submission_ready should be True
    assert report_pass["attestation"]["submission_ready"] is True

    # no FAIL findings should remain
    assert_no_fail_findings(report_pass)

    # previously failing code CORE.ID.UNMATCHED_SAMPLE must be gone
    pass_codes = extract_codes(report_pass)
    assert "CORE.ID.UNMATCHED_SAMPLE" not in pass_codes
