# Run ablation_alpha_0p0_mvtec_bottle_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9895316790070026`
- `auroc`: `0.9706349206349206`
- `brier`: `0.24962497095752834`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4128791901720576`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023555702428860836`
- `max_f1`: `0.9612403100775194`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6923491591603548`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_bottle_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
