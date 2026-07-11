# Run ablation_calib_upper_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9502233041947811`
- `auroc`: `0.9065226422933111`
- `brier`: `0.18479816841218843`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.16430213212544192`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002066980188725688`
- `max_f1`: `0.8903225806451613`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5029876085148935`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
