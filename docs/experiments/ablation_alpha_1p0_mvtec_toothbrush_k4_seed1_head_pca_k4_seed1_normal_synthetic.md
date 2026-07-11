# Run ablation_alpha_1p0_mvtec_toothbrush_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9415445547238716`
- `auroc`: `0.8402777777777778`
- `brier`: `0.20152049176697112`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.009943834372929117`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003828688036827814`
- `max_f1`: `0.8955223880597015`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5919901501025542`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
