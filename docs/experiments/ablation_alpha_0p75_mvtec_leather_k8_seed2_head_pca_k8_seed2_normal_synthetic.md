# Run ablation_alpha_0p75_mvtec_leather_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_leather_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.16642390480401073`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22426313450259547`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029974670840367196`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5152302594711822`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_leather_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
