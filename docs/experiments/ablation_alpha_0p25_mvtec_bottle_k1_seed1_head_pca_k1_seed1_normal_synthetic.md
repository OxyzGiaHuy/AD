# Run ablation_alpha_0p25_mvtec_bottle_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9745784839354895`
- `auroc`: `0.9373015873015873`
- `brier`: `0.21770777207451059`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28055484539054965`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002747316182736891`
- `max_f1`: `0.9538461538461539`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6282115997732998`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
