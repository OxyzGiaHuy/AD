# Run ablation_calib_upper_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9935348752653128`
- `auroc`: `0.9800347222222222`
- `brier`: `0.04441516979645802`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.07316823944981614`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014218147045799664`
- `max_f1`: `0.9771689497716894`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.1621064335594284`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
