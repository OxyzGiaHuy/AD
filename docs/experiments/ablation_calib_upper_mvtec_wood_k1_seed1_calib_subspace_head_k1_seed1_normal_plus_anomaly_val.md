# Run ablation_calib_upper_mvtec_wood_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9475649069161215`
- `auroc`: `0.8771929824561403`
- `brier`: `0.15526673785839118`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.17741318781898446`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002819200288759519`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6905425344417171`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
