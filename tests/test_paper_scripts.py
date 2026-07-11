import json
import sys

import numpy as np

from scripts import aggregate_paper_tables
from src.robustness.corruptions import brightness_contrast, gaussian_noise, jpeg


def test_aggregate_paper_tables_mean_std(tmp_path, monkeypatch, capsys):
    for seed, auroc in [(0, 0.8), (1, 1.0)]:
        run = tmp_path / f"calib_subspace_mvtec_bottle_k1_seed{seed}_calib_subspace_head"
        run.mkdir()
        (run / "metrics.json").write_text(json.dumps({"auroc": auroc, "ap": 0.5}), encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["aggregate_paper_tables.py", "--outputs-dir", str(tmp_path), "--pattern", "*"])
    assert aggregate_paper_tables.main() == 0
    out = capsys.readouterr().out
    assert "0.9000+-0.1000" in out


def test_corruptions_preserve_shape_and_range():
    image = np.full((8, 8, 3), 0.5, dtype=np.float32)
    for corrupted in [gaussian_noise(image, seed=0), brightness_contrast(image), jpeg(image)]:
        assert corrupted.shape == image.shape
        assert corrupted.min() >= 0.0
        assert corrupted.max() <= 1.0
