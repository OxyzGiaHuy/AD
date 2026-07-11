# Run ablation_calib_upper_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9760986204119139`
- `auroc`: `0.8933979406420351`
- `brier`: `0.14001241805541767`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.1402740525264366`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025705920008857264`
- `max_f1`: `0.9372693726937269`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4873357784567457`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
