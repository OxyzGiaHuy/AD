# Run ablation_alpha_1p0_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9356962881794597`
- `auroc`: `0.8783733133433284`
- `brier`: `0.2576018306698752`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14667003194491068`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00383265578498443`
- `max_f1`: `0.8554913294797688`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7172579232066244`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
