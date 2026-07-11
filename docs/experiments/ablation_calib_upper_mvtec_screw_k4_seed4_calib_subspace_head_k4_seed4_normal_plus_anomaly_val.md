# Run ablation_calib_upper_mvtec_screw_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.777854108153924`
- `auroc`: `0.6257904245709124`
- `brier`: `0.2259377757733668`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.2226626208464571`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016279749247251742`
- `max_f1`: `0.8536585365853658`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.9268860265007297`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
