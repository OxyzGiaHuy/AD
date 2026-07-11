# Run ablation_alpha_0p0_mvtec_cable_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9594299097459521`
- `auroc`: `0.9179160419790104`
- `brier`: `0.24052432644750998`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11971179942289983`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0031195348377029103`
- `max_f1`: `0.896551724137931`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6741842140965546`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
