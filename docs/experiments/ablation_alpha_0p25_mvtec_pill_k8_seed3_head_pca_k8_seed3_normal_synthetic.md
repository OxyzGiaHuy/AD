# Run ablation_alpha_0p25_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9868421961125897`
- `auroc`: `0.9358974358974359`
- `brier`: `0.19792446617433507`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3349907740861356`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019006159290403664`
- `max_f1`: `0.9480968858131488`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5881443392828019`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
