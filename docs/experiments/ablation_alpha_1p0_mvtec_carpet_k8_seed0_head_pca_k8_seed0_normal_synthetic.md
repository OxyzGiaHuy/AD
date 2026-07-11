# Run ablation_alpha_1p0_mvtec_carpet_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9884969560856726`
- `auroc`: `0.96669341894061`
- `brier`: `0.14510745158756835`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26078652571409183`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025141176282085925`
- `max_f1`: `0.9726775956284153`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4639363083008617`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
