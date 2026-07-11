# Run ablation_calib_upper_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9849557830824616`
- `auroc`: `0.9318594791035736`
- `brier`: `0.13271357543331827`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.1308963345546348`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001544208113664116`
- `max_f1`: `0.9442379182156134`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.41341111497301014`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
