# Run ablation_alpha_0p75_mvtec_bottle_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.986203148965481`
- `auroc`: `0.9634920634920635`
- `brier`: `0.1711576106791241`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08682626198573282`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002072378589087222`
- `max_f1`: `0.9682539682539683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5259446841454989`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_bottle_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
