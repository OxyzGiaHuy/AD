# Run ablation_alpha_1p0_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9888945354861227`
- `auroc`: `0.960609243697479`
- `brier`: `0.15005138852946714`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22318912144528316`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002146623374906597`
- `max_f1`: `0.9590163934426229`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4765797613909652`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
