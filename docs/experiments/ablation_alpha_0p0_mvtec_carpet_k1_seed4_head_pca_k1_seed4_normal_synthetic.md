# Run ablation_alpha_0p0_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_carpet_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9998751560549313`
- `auroc`: `0.9995987158908507`
- `brier`: `0.2299529356193258`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2599551295622801`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004133308783937723`
- `max_f1`: `0.994413407821229`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6530040165592`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
