# Run ablation_alpha_1p0_mvtec_leather_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9843043121576421`
- `auroc`: `0.9539741847826086`
- `brier`: `0.19148612885057523`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.022967371248429846`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020177521322283054`
- `max_f1`: `0.93048128342246`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5711002719598497`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
