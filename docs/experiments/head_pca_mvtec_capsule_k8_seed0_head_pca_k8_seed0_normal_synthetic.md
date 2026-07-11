# Run head_pca_mvtec_capsule_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9388635802988127`
- `auroc`: `0.7750299162345433`
- `brier`: `0.24445431012142896`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34410919452255423`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015743653656858387`
- `max_f1`: `0.9237668161434978`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6820356908626487`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_capsule_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
