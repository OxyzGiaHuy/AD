# Run ablation_calib_upper_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.905713732839579`
- `auroc`: `0.859920634920635`
- `brier`: `0.326577632249143`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.34019796304332406`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014165122676821588`
- `max_f1`: `0.8484848484848485`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1011315903983516`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
