# Run ablation_alpha_1p0_mvtec_leather_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9972795277165164`
- `auroc`: `0.9915081521739131`
- `brier`: `0.17654907635848088`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35360058613361844`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028409381367025836`
- `max_f1`: `0.9732620320855615`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5352491896533204`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
