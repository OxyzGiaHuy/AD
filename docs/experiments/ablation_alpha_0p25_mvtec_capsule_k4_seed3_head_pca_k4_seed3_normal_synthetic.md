# Run ablation_alpha_0p25_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9716606120363994`
- `auroc`: `0.8815317112086158`
- `brier`: `0.20453296788862785`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.279796643013304`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00274147709944483`
- `max_f1`: `0.9292035398230089`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6015133070228209`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
