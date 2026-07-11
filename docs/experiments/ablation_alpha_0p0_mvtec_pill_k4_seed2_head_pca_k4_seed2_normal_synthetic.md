# Run ablation_alpha_0p0_mvtec_pill_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_pill_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9865950794258949`
- `auroc`: `0.9367157665030006`
- `brier`: `0.23539419952892374`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3402117476491871`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002613658096618995`
- `max_f1`: `0.9583333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6638967081866131`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_pill_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
