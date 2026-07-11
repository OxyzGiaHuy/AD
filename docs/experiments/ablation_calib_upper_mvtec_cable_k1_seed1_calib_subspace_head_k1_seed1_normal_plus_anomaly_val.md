# Run ablation_calib_upper_mvtec_cable_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9037490404379387`
- `auroc`: `0.8452430411300373`
- `brier`: `0.36422576310530885`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.374750571048006`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013925838977732557`
- `max_f1`: `0.8024691358024691`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.276591975239394`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
