# Run ablation_calib_upper_mvtec_zipper_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9851268223031303`
- `auroc`: `0.9513888888888888`
- `brier`: `0.0990470512208594`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.11456090789288287`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022153309546411037`
- `max_f1`: `0.9459459459459459`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.32035283349363664`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
