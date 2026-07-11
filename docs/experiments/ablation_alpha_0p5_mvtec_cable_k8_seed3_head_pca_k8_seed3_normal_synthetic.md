# Run ablation_alpha_0p5_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9398847100029258`
- `auroc`: `0.881184407796102`
- `brier`: `0.228436156281977`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05491405367851252`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022537321597337723`
- `max_f1`: `0.8786127167630058`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6487663755416296`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
