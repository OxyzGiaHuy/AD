# Run ablation_pca64_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_grid_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9923125935512159`
- `auroc`: `0.9807852965747702`
- `brier`: `0.23294754621431218`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23932998574888092`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030428158979003248`
- `max_f1`: `0.9743589743589743`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.0689230803377163`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
