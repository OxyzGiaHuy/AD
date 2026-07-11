# Run ablation_alpha_0p0_mvtec_carpet_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_carpet_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9994920791527584`
- `auroc`: `0.9983948635634029`
- `brier`: `0.2546119392889788`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4643354726652814`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005764861758320759`
- `max_f1`: `0.994413407821229`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7016931565922393`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_carpet_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
