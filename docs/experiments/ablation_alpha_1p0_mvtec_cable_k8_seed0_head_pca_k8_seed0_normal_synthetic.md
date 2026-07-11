# Run ablation_alpha_1p0_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9499967652565352`
- `auroc`: `0.901424287856072`
- `brier`: `0.2484470272418442`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13557002822558084`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032496546705563863`
- `max_f1`: `0.8771929824561403`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6937056708649378`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
