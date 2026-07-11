# Run ablation_alpha_1p0_mvtec_grid_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9527938553981662`
- `auroc`: `0.8638262322472848`
- `brier`: `0.18606882074452835`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1315577557453742`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002484581075035609`
- `max_f1`: `0.8870967741935484`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5580400615211808`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
