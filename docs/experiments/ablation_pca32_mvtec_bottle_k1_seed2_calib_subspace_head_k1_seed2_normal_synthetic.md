# Run ablation_pca32_mvtec_bottle_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9597790878876479`
- `auroc`: `0.9055555555555556`
- `brier`: `0.24095514796086345`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24095949422882268`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002386411427553878`
- `max_f1`: `0.9365079365079365`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.740969621145291`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
