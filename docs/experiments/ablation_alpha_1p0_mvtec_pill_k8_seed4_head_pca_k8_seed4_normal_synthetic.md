# Run ablation_alpha_1p0_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9773973217932124`
- `auroc`: `0.9075286415711947`
- `brier`: `0.13145184535423723`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2295156442476604`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001802684750385627`
- `max_f1`: `0.9448275862068966`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.437737054228405`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
