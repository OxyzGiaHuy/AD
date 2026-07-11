# Run ablation_calib_upper_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9996371552975327`
- `auroc`: `0.9990842490842491`
- `brier`: `0.01332092986550102`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.04626475957107465`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021676741132180986`
- `max_f1`: `0.9904761904761905`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.057178022704927146`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
