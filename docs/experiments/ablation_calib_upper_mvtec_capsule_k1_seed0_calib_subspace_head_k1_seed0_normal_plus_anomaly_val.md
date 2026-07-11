# Run ablation_calib_upper_mvtec_capsule_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9515982895612429`
- `auroc`: `0.826526130873957`
- `brier`: `0.1355940678598956`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.1265139655500162`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019452801798699332`
- `max_f1`: `0.9238095238095239`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4754827199657862`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
