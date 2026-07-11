# Run ablation_pca64_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9907719851443024`
- `auroc`: `0.9549918166939444`
- `brier`: `0.08771531036967169`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09651147993560322`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00226098754091891`
- `max_f1`: `0.9608540925266904`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.37572086719407893`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
