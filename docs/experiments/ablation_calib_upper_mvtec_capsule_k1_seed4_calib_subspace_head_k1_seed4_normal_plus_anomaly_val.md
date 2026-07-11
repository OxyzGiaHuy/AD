# Run ablation_calib_upper_mvtec_capsule_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9575660674730196`
- `auroc`: `0.8555116381203338`
- `brier`: `0.16959034376661977`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.16826505836893302`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026614318800265674`
- `max_f1`: `0.9346733668341709`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6417434399778646`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
