# Run ablation_alpha_0p0_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9847970574021614`
- `auroc`: `0.957936507936508`
- `brier`: `0.2432174627851871`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2726369058511343`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005051845011402325`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6795721898001408`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
