# Run ablation_alpha_0p25_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9610934180286688`
- `auroc`: `0.9218515742128935`
- `brier`: `0.22837134678588691`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1261835165818532`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023033960287769635`
- `max_f1`: `0.8994082840236687`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6494720474630906`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
