# Run ablation_alpha_0p25_mvtec_transistor_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8277496708375992`
- `auroc`: `0.8758333333333334`
- `brier`: `0.2520781573758279`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14859039217233658`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025725664012134076`
- `max_f1`: `0.775`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6972136321794555`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
