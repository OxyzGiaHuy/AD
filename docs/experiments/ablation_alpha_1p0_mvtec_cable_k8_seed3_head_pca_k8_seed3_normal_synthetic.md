# Run ablation_alpha_1p0_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9450712007968215`
- `auroc`: `0.8847451274362819`
- `brier`: `0.24938249873045232`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12851001501083376`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017501523594061533`
- `max_f1`: `0.8875739644970414`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6958699582177106`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
