# Run ablation_alpha_1p0_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9954652402941361`
- `auroc`: `0.9857142857142858`
- `brier`: `0.1574114868198483`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25057193600987815`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004322482991110848`
- `max_f1`: `0.96875`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4906415676062147`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
