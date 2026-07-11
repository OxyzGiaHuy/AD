# Run ablation_alpha_0p5_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9710640753203449`
- `auroc`: `0.8815317112086158`
- `brier`: `0.1732620673195441`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23922345132538764`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003156060084813472`
- `max_f1`: `0.9259259259259259`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5357778855380796`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
