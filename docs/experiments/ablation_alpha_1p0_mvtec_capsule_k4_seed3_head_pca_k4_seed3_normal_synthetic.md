# Run ablation_alpha_1p0_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9571586983707424`
- `auroc`: `0.8264858396489828`
- `brier`: `0.14405183825687673`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1691756230412107`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0029697597280822015`
- `max_f1`: `0.9316239316239316`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4661586297441427`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
