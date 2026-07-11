# Run ablation_alpha_1p0_mvtec_cable_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8177476675933751`
- `auroc`: `0.6993065967016492`
- `brier`: `0.2501348310617009`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11411476453145353`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004279700256884098`
- `max_f1`: `0.7659574468085106`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6977007426080769`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
