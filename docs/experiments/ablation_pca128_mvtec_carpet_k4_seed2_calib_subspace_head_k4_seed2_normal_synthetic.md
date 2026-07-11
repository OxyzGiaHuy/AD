# Run ablation_pca128_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9995073634751871`
- `auroc`: `0.9983948635634029`
- `brier`: `0.09855815687446023`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12933717012150675`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002359530036775475`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.47289637145809155`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
