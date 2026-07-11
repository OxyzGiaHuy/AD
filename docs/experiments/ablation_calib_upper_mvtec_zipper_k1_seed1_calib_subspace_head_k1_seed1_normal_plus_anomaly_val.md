# Run ablation_calib_upper_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9835850965464272`
- `auroc`: `0.9490740740740741`
- `brier`: `0.14670238835552274`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.16510018557310108`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020929312599556786`
- `max_f1`: `0.9469026548672567`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.45269909883822956`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
