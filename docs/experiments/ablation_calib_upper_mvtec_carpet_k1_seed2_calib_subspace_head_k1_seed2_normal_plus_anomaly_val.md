# Run ablation_calib_upper_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9980264976452414`
- `auroc`: `0.9942680776014109`
- `brier`: `0.05122200142954909`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.08268776877757605`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025136527699341467`
- `max_f1`: `0.9818181818181818`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.1792535828683736`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
