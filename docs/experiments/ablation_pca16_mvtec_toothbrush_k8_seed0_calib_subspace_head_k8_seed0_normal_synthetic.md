# Run ablation_pca16_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9714102164285116`
- `auroc`: `0.925`
- `brier`: `0.10006935553073741`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14926263485990815`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004033234857377552`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3385291163438745`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
