# Run ablation_alpha_1p0_mvtec_bottle_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_bottle_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9940202063000149`
- `auroc`: `0.9801587301587301`
- `brier`: `0.1702928085682336`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20266458571675317`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0036335225968834864`
- `max_f1`: `0.953125`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5223306274281065`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_bottle_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
