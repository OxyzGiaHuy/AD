# Run smoke_synthetic_upper_bound_head_pca_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/experiments/smoke_synthetic_upper_bound.yaml`
- Dataset: `synthetic`
- Model: `head_pca`

## Metrics

- `ap`: `0.42063492063492064`
- `auroc`: `0.25`
- `brier`: `0.24003012437149845`
- `calibration_anomaly_val_count`: `1`
- `ece`: `0.19735964281218388`
- `k_shot`: `1`
- `latency_sec_per_image`: `1.4783282365117754e-05`
- `max_f1`: `0.6`
- `model_storage_mb`: `0.000736236572265625`
- `nll`: `0.6731696672446795`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `16`

## Notes

- Predictions written to outputs/smoke_synthetic_upper_bound_head_pca_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
