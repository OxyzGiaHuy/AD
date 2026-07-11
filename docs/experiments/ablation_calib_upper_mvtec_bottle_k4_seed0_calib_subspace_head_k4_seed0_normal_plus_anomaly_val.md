# Run ablation_calib_upper_mvtec_bottle_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9988003322156941`
- `auroc`: `0.9964912280701754`
- `brier`: `0.02938327822205095`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.0830868787386201`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027449724155587034`
- `max_f1`: `0.9827586206896551`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.11478879091528942`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
