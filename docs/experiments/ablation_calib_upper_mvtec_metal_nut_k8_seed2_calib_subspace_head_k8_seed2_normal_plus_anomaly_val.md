# Run ablation_calib_upper_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9966069517728554`
- `auroc`: `0.9864718614718615`
- `brier`: `0.0770137638621984`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.08352210661308532`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023495193641140774`
- `max_f1`: `0.9761904761904762`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2813793125186613`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
