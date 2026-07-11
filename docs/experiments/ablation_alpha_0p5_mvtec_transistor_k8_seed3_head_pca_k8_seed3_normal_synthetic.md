# Run ablation_alpha_0p5_mvtec_transistor_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8391570253852748`
- `auroc`: `0.8829166666666667`
- `brier`: `0.27357002455712154`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20996766090393065`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003007899709045887`
- `max_f1`: `0.7894736842105263`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7407959896157587`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_transistor_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
