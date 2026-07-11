# Run ablation_pca64_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_metal_nut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9956145197304783`
- `auroc`: `0.9809384164222874`
- `brier`: `0.09527323761017108`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10895887362446803`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016775173823470654`
- `max_f1`: `0.968421052631579`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6160122407898424`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
