# Run ablation_calib_upper_mvtec_cable_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9519400951911898`
- `auroc`: `0.9129621936019942`
- `brier`: `0.23953726199356784`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.27097027183424494`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002548802789327101`
- `max_f1`: `0.8846153846153846`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6386267134115261`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
