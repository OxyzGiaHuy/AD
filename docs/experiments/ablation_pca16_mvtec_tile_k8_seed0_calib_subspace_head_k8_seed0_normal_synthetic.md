# Run ablation_pca16_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9936829210676014`
- `auroc`: `0.9852092352092352`
- `brier`: `0.08463624050244413`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12514782225729054`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002728566638806946`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2583965147446105`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
