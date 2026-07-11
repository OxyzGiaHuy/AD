# Run ablation_calib_upper_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9817001927876667`
- `auroc`: `0.9218269653052261`
- `brier`: `0.10053693381610349`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.09746419221208598`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021836182682729156`
- `max_f1`: `0.9371980676328503`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3725603873554091`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
