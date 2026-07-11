# Run ablation_calib_upper_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9792804069615237`
- `auroc`: `0.9614035087719298`
- `brier`: `0.06905247100092218`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.11051855516898168`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0033360877158966932`
- `max_f1`: `0.9739130434782609`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2491955374100547`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
