# Run ablation_alpha_0p5_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9859295690678552`
- `auroc`: `0.930987452264048`
- `brier`: `0.16675488537593688`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29147396223273825`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020844451748503897`
- `max_f1`: `0.9484536082474226`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5224744929712074`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
