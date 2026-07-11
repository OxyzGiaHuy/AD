# Run ablation_alpha_0p0_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.998442758557556`
- `auroc`: `0.9931573802541545`
- `brier`: `0.2540578784345171`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.43707890510559083`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032472762076751044`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7011993565599351`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
