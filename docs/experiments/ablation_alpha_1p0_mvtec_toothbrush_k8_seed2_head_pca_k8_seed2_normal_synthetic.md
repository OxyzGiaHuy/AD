# Run ablation_alpha_1p0_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9466435211002354`
- `auroc`: `0.8777777777777778`
- `brier`: `0.19951993286544367`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.023581216732660885`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005985749175860768`
- `max_f1`: `0.9090909090909091`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5872641770801436`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
