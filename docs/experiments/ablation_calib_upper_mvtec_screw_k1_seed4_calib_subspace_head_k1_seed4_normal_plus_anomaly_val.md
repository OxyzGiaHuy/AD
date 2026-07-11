# Run ablation_calib_upper_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7502331387208035`
- `auroc`: `0.575880758807588`
- `brier`: `0.2516598496100335`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.2443576319105673`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002055388206503535`
- `max_f1`: `0.8492063492063492`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1941602787438337`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
