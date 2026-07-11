# Run ablation_alpha_0p25_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9242544227459996`
- `auroc`: `0.8611319340329835`
- `brier`: `0.23593554690215085`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06084815859794612`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019469700505336126`
- `max_f1`: `0.8361581920903954`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6648431349645849`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
