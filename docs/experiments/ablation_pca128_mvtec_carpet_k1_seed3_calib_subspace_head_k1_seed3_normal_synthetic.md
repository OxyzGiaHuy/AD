# Run ablation_pca128_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9980017191642448`
- `auroc`: `0.9935794542536116`
- `brier`: `0.1800684901797955`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2051426360749791`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002784070184724963`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7900814825053782`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
