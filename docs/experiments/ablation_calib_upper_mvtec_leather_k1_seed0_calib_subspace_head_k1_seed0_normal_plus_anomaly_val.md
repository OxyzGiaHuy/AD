# Run ablation_calib_upper_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_leather_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9979260172116146`
- `auroc`: `0.9947289156626506`
- `brier`: `0.07281323307908436`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.10077830326298008`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025593113964018613`
- `max_f1`: `0.9880952380952381`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2208295937896074`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
