# Run ablation_calib_upper_mvtec_screw_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7605911767215962`
- `auroc`: `0.5788166214995484`
- `brier`: `0.2630016043359731`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.26354630881507923`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003049371851570654`
- `max_f1`: `0.8524590163934426`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.402097226140284`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
