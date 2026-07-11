# Few-Shot Robust Calibrated Anomaly Detection

Research scaffold for frozen DINOv2 few-shot anomaly detection with small
trainable heads/adapters, PCA residual scoring, calibration, robustness
evaluation, and reproducible experiment notes.

## Main CLIs

```bash
python -m src.run_experiment --config configs/experiments/headpca_mvtec.yaml
python -m src.extract_features --dataset mvtec --root /path/to/mvtec --k-shot 4
python -m src.evaluate_robustness --run-id <run_id> --attack fgsm --epsilon 8/255
```

## Dataset Download

Because `/home` can be small on shared machines, download large datasets to a
separate location and symlink them into `data/`:

```bash
python scripts/download_datasets.py --dataset visa --download-root /tmp/AD-data

# MVTec requires accepting the official license/form first, then passing the URL:
python scripts/download_datasets.py --dataset mvtec --mvtec-url "<official-mvtec-url>" --download-root /tmp/AD-data

# Kaggle mirror, requires Kaggle API token in ~/.kaggle/kaggle.json:
python scripts/download_datasets.py --dataset mvtec_kaggle --download-root /tmp/AD-data
```

## Tests

Run tests from the repo root:

```bash
python -m pytest -q
# or, if your shell has ROS pytest plugins on PYTHONPATH:
scripts/run_tests.sh
```

The repo includes `sitecustomize.py` to disable auto-loading unrelated global
pytest plugins, such as ROS `launch_testing`, which can break isolated conda
environments before project tests are collected.

## Outputs

Each experiment writes:

- `metrics.json`
- `predictions.parquet` when pandas/pyarrow are installed, otherwise CSV
- `anomaly_maps/`
- `docs/experiments/<run_id>.md`

Keep research observations in `docs/research_log.md`, install problems in
`docs/setup_issues.md`, and benchmark decisions in
`docs/benchmark_protocol.md`.

