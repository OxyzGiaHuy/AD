# Run ablation_alpha_1p0_mvtec_zipper_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9975924297697636`
- `auroc`: `0.9908088235294118`
- `brier`: `0.1645261902116827`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12057199620253195`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002618245669449402`
- `max_f1`: `0.9714285714285714`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5117136323213061`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
