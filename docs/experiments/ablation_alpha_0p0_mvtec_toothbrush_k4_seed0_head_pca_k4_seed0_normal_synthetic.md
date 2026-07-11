# Run ablation_alpha_0p0_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9696799983139461`
- `auroc`: `0.9277777777777778`
- `brier`: `0.249122129421451`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4075962134769984`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004940004487122808`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6913461655764974`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_toothbrush_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
