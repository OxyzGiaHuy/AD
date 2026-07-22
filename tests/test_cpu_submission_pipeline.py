import json

import pandas as pd

from scripts.run_cpu_submission_pipeline import run_pipeline


def test_cpu_submission_pipeline_audits_runs_and_hashes_outputs(tmp_path):
    views = []
    stats = []
    support = []
    residuals = []
    for class_index in range(7):
        cls = f"c{class_index}"
        stats.append({
            "dataset": "toy", "class": cls, "k_shot": 2, "seed": 0,
            "support_calibration_mode": "loio_conformal",
            "support_cal_median": 0.2, "support_cal_mad": 0.1,
            "support_cal_q25": 0.1, "support_cal_q75": 0.3,
            "support_cal_count": 2,
        })
        for support_index in range(2):
            support.append({
                "dataset": "toy", "class": cls, "k_shot": 2, "seed": 0,
                "support_index": support_index,
                "image_path": f"/toy/{cls}/train/{support_index}.png",
            })
            residuals.append({
                "dataset": "toy", "class": cls, "k_shot": 2, "seed": 0,
                "loio_residual": 0.1 + 0.1 * support_index,
            })
        for image_index, label in enumerate([0, 0, 1, 1]):
            path = f"/toy/{cls}/test/{image_index}.png"
            views.append({
                "dataset": "toy", "class": cls, "k_shot": 2, "seed": 0,
                "corruption": "clean", "base_image_path": path,
                "image_path": path, "label": label,
                "raw_score": 0.1 * image_index + label,
                "sampling_protocol": "label_stratified_random",
                "sampling_seed": 0, "max_images": 4,
                "corruption_parameters": "none",
            })
    paths = {}
    for name, frame in {
        "views": pd.DataFrame(views), "stats": pd.DataFrame(stats),
        "support": pd.DataFrame(support), "residuals": pd.DataFrame(residuals),
    }.items():
        paths[name] = tmp_path / f"{name}.csv"
        frame.to_csv(paths[name], index=False)
    config = {
        "run_tag": "toy_run", "out_dir": str(tmp_path / "out"),
        "grid": {"k_shots": [2], "seeds": [0], "corruptions": ["clean"]},
        "alphas": [0.2], "delta": 0.05, "max_candidates": 5,
        "bootstrap_iterations": 100, "bootstrap_seed": 0, "family_alpha": 0.05,
        "artifact_sets": {"toy": {
            "views": str(paths["views"]), "support_stats": str(paths["stats"]),
            "support_manifest": str(paths["support"]),
            "support_residuals": str(paths["residuals"]),
        }},
        "jobs": [{
            "id": "toy_within", "artifact_sets": ["toy"],
            "target_dataset": "toy", "source_modes": ["matched_condition"],
        }],
        "analyses": [{"id": "primary", "normalization": "median_mad", "confirmatory": True}],
    }
    config_path = tmp_path / "pipeline.json"
    config_path.write_text(json.dumps(config), encoding="utf-8")
    manifest_path = run_pipeline(config_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["artifact_audits"]["toy"]["status"] == "pass"
    assert manifest["runs"][0]["methods"] == [
        "nested_sc3r", "pooled_source_conformal", "target_only"
    ]
    assert len(manifest["outputs"]) == 9
    assert manifest["confirmatory_family"]["family_size"] > 0
    assert manifest["empirical_target_gate"]["n_gate_cells"] > 0
    assert manifest["empirical_target_gate"]["n_empirical_fail"] > 0
    assert all(len(record["sha256"]) == 64 for record in manifest["outputs"].values())
