# Run ablation_calib_upper_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7837289133450079`
- `auroc`: `0.8347222222222223`
- `brier`: `0.36134545966238996`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.42372052821641165`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002569458835447828`
- `max_f1`: `0.7272727272727273`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2033392323404657`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
