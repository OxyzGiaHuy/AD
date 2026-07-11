# Run ablation_calib_upper_mvtec_cable_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9337241723831559`
- `auroc`: `0.8818030743664312`
- `brier`: `0.3746060762531443`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.38587127763328827`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0035575693935578595`
- `max_f1`: `0.8518518518518519`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.4193284994432713`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
