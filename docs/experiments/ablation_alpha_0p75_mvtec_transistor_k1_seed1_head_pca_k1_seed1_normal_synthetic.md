# Run ablation_alpha_0p75_mvtec_transistor_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8143063705191395`
- `auroc`: `0.7966666666666666`
- `brier`: `0.31446018196486764`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27516436338424677`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020686909928917885`
- `max_f1`: `0.72`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8289196429381773`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
