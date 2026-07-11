# Run ablation_alpha_0p5_mvtec_transistor_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.760715581647`
- `auroc`: `0.8075`
- `brier`: `0.28412857263242836`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21648286104202263`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019241296872496605`
- `max_f1`: `0.7291666666666666`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7627283243682588`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_transistor_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
