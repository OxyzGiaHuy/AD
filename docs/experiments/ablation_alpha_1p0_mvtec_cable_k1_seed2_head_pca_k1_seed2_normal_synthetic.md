# Run ablation_alpha_1p0_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8166443202187127`
- `auroc`: `0.7076461769115442`
- `brier`: `0.24761328382253442`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10236244519551596`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002021065279841423`
- `max_f1`: `0.774468085106383`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6914248163012854`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
