# Run ablation_alpha_1p0_mvtec_tile_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9902924158963022`
- `auroc`: `0.977994227994228`
- `brier`: `0.1811554090562641`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14109606416816386`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002146319955842108`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5424199956572683`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
