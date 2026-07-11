# Run ablation_pca128_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9519297035737132`
- `auroc`: `0.9`
- `brier`: `0.28533433284658694`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2855233266240075`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0040049976447508445`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.079326754389598`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
