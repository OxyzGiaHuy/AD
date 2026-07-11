# Run ablation_calib_upper_mvtec_toothbrush_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9892016008682676`
- `auroc`: `0.9753086419753086`
- `brier`: `0.21610011142719676`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.24516759812831876`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004313264233179581`
- `max_f1`: `0.9473684210526315`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.8547741616650865`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
