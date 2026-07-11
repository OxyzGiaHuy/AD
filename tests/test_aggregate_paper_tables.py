import json
import sys
from pathlib import Path

from scripts.aggregate_paper_tables import parse_run_id, fmt
from scripts import aggregate_robustness


def test_parse_run_id_and_fmt():
    info = parse_run_id("calib_subspace_mvtec_bottle_calib_subspace_head_k1_seed0_normal_synthetic")
    assert info["dataset"] == "mvtec"
    assert info["variant"] == "calib_subspace_head"
    assert info["k_shot"] == "1"
    assert info["calibration_mode"] == "normal_synthetic"
    assert info["experiment"] == "calib_subspace_mvtec_bottle"
    assert fmt([1.0, 3.0]).startswith("2.0000+-")

def test_aggregate_robustness_outputs_drop_table(tmp_path, monkeypatch):
    clean = tmp_path / "outputs" / "calib_subspace_head_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic"
    corrupt = tmp_path / "outputs" / "robustness" / "calib_subspace_head_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_gaussian_noise"
    clean.mkdir(parents=True)
    corrupt.mkdir(parents=True)
    (clean / "metrics.json").write_text(json.dumps({"auroc": 1.0, "ap": 0.9, "ece": 0.1, "brier": 0.2, "nll": 0.3}), encoding="utf-8")
    (corrupt / "metrics.json").write_text(json.dumps({"auroc": 0.8, "ap": 0.7, "ece": 0.15, "brier": 0.25, "nll": 0.4}), encoding="utf-8")
    out_dir = tmp_path / "tables"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "aggregate_robustness.py",
            "--outputs-dir",
            str(tmp_path / "outputs"),
            "--robustness-dir",
            str(tmp_path / "outputs" / "robustness"),
            "--out-dir",
            str(out_dir),
        ],
    )
    assert aggregate_robustness.main() == 0
    summary = (out_dir / "mvtec_calib_subspace_head_robustness_summary.md").read_text(encoding="utf-8")
    assert "gaussian_noise" in summary
    assert "0.2000 +/- 0.0000" in summary

