import hashlib
import json

from scripts.audit_submission_package import (
    _latex_word_count,
    _verify_cpu_manifest,
    audit_submission,
)


def test_latex_word_count_ignores_commands_and_braces():
    assert _latex_word_count(r"A \textbf{short} abstract with $k=4$ and \cite{x}.") == 7


def test_submission_audit_fails_closed_on_missing_manifest_and_placeholders(tmp_path):
    (tmp_path / "sections").mkdir()
    (tmp_path / "tables").mkdir()
    (tmp_path / "main.tex").write_text("First Author\\author@example.com", encoding="utf-8")
    (tmp_path / "sections" / "abstract.tex").write_text("short abstract", encoding="utf-8")
    (tmp_path / "cover_letter.md").write_text("cover", encoding="utf-8")
    report = audit_submission(tmp_path)
    assert report["status"] == "fail"
    assert "placeholder author" in report["issues"]
    assert "placeholder email" in report["issues"]
    assert "final CPU pipeline manifest was not supplied" in report["issues"]


def test_cpu_manifest_artifacts_rebase_to_a_moved_checkout(tmp_path):
    artifact = tmp_path / "outputs" / "submission_cpu" / "paired_cells.csv"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("value\n1\n", encoding="utf-8")
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    old_root = "/server/original/AD"
    record = {
        "path": f"{old_root}/outputs/submission_cpu/paired_cells.csv",
        "sha256": digest,
    }
    manifest = {
        "config": f"{old_root}/configs/submission.json",
        "artifact_audits": {"dataset": {"status": "pass"}},
        "runs": [{
            "tag": "run",
            "methods": ["target_only", "pooled_source_conformal", "nested_sc3r"],
        }],
        "confirmatory_family": {"multiplicity": "bonferroni", "family_size": 1},
        "empirical_target_gate": {"n_gate_cells": 1},
        "inputs": {"input_paired_cells": record},
        "outputs": {
            "paired_cells.csv": record,
            "result_summary.csv": record,
            "empirical_gate.json": record,
        },
        "environment": {"git": {"commit": "abc123", "dirty": False}},
    }
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    assert _verify_cpu_manifest(manifest_path, tmp_path) == []
