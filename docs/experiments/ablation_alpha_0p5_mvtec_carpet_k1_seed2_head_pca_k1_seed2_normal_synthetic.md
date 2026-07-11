# Run ablation_alpha_0p5_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9897940651861209`
- `auroc`: `0.9658908507223114`
- `brier`: `0.18825130316751654`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.354482864212786`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004457122654232205`
- `max_f1`: `0.9550561797752809`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5668800343354182`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
