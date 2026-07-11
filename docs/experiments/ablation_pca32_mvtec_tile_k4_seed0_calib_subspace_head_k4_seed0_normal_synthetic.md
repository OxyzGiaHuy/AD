# Run ablation_pca32_mvtec_tile_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9924368927386776`
- `auroc`: `0.9823232323232324`
- `brier`: `0.18762385165378884`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15493647696880194`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025598217979965047`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.7623168256464992`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
