# Run ablation_calib_upper_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9927671994984192`
- `auroc`: `0.9745670995670995`
- `brier`: `0.08647114205070074`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.11054120353370342`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032610409137494157`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2814214057939226`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
