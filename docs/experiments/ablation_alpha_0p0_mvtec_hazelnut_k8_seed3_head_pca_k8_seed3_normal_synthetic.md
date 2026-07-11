# Run ablation_alpha_0p0_mvtec_hazelnut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9917371298914426`
- `auroc`: `0.9875`
- `brier`: `0.23511076751085444`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1643490374088287`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0031020656736059624`
- `max_f1`: `0.9784172661870504`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6633428425665541`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_hazelnut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
