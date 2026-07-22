import pandas as pd

from scripts.audit_sc3r_artifacts import audit_frames


def _frames():
    views = pd.DataFrame(
        [
            {
                "dataset": "toy",
                "class": "a",
                "k_shot": 2,
                "seed": 0,
                "corruption": "clean",
                "base_image_path": f"/data/a/test/{index}.png",
                "image_path": f"/data/a/test/{index}.png",
                "label": index,
                "raw_score": 0.1 + index,
                "sampling_protocol": "label_stratified_random",
                "sampling_seed": 0,
                "max_images": 2,
                "corruption_parameters": "none",
            }
            for index in (0, 1)
        ]
    )
    stats = pd.DataFrame(
        [{"dataset": "toy", "class": "a", "k_shot": 2, "seed": 0, "support_calibration_mode": "loio_conformal", "support_cal_median": 0.2, "support_cal_mad": 0.1, "support_cal_q25": 0.1, "support_cal_q75": 0.3, "support_cal_count": 2}]
    )
    support = pd.DataFrame(
        [
            {"dataset": "toy", "class": "a", "k_shot": 2, "seed": 0, "support_index": index, "image_path": f"/data/a/train/{index}.png"}
            for index in (0, 1)
        ]
    )
    return views, stats, support


def test_artifact_audit_passes_consistent_frames():
    summary = audit_frames(*_frames())
    assert summary["status"] == "pass"
    assert summary["n_view_cells"] == 1


def test_artifact_audit_detects_support_test_overlap():
    views, stats, support = _frames()
    support.loc[0, "image_path"] = views.loc[0, "base_image_path"]
    summary = audit_frames(views, stats, support)
    assert summary["status"] == "fail"
    assert any("leakage" in issue for issue in summary["issues"])


def test_artifact_audit_detects_duplicate_base_image_cell():
    views, stats, support = _frames()
    views = pd.concat([views, views.iloc[[0]]], ignore_index=True)
    summary = audit_frames(views, stats, support)
    assert summary["status"] == "fail"
    assert any("duplicate" in issue for issue in summary["issues"])


def test_artifact_audit_detects_unpaired_corruption_base_images():
    views, stats, support = _frames()
    jpeg = views.copy()
    jpeg["corruption"] = "jpeg"
    jpeg["corruption_parameters"] = "quality=60"
    jpeg.loc[0, "base_image_path"] = "/data/a/test/different.png"
    summary = audit_frames(pd.concat([views, jpeg], ignore_index=True), stats, support)
    assert summary["status"] == "fail"
    assert any("base-image sets differ" in issue for issue in summary["issues"])


def test_artifact_audit_checks_expected_grid_and_finite_scores():
    views, stats, support = _frames()
    views.loc[0, "raw_score"] = float("inf")
    summary = audit_frames(
        views, stats, support,
        expected_k_shots=[1, 2], expected_seeds=[0, 1], expected_corruptions=["clean", "jpeg"],
    )
    assert summary["status"] == "fail"
    assert any("non-finite" in issue for issue in summary["issues"])
    assert any("grid mismatch" in issue for issue in summary["issues"])
