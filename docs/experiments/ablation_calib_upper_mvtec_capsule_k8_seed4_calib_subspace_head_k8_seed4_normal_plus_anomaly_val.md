# Run ablation_calib_upper_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9640487893607179`
- `auroc`: `0.8801054018445322`
- `brier`: `0.10770397060638673`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.08324986653494054`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013734576765631066`
- `max_f1`: `0.941747572815534`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3842728112848286`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
