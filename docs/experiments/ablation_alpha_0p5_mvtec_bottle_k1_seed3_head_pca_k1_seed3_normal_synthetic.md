# Run ablation_alpha_0p5_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9956134653170479`
- `auroc`: `0.9857142857142858`
- `brier`: `0.1948196998558031`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2396609890891845`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027716411389859326`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5804494964244453`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
