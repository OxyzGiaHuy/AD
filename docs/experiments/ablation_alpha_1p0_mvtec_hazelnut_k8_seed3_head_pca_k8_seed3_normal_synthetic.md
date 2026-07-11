# Run ablation_alpha_1p0_mvtec_hazelnut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9662591658843591`
- `auroc`: `0.9332142857142857`
- `brier`: `0.23991034047525434`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10765954689546071`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030790456316687844`
- `max_f1`: `0.9037037037037037`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6758081991111815`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
