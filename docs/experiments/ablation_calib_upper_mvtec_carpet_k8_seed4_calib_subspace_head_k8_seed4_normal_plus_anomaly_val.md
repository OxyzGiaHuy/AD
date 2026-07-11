# Run ablation_calib_upper_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9989754911864683`
- `auroc`: `0.9969135802469136`
- `brier`: `0.03141449887720281`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.07132626117266917`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002406817989065013`
- `max_f1`: `0.9876543209876543`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.11070880027161965`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
