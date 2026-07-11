# Run ablation_alpha_0p75_mvtec_grid_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9625492175185572`
- `auroc`: `0.8863826232247285`
- `brier`: `0.19187647220720686`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23625677824020386`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0032896252874380504`
- `max_f1`: `0.8870967741935484`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5726575526300816`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
