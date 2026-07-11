# Run ablation_pca16_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9915219936068016`
- `auroc`: `0.9736842105263158`
- `brier`: `0.17840341797950057`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1972544975578785`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026703942331332193`
- `max_f1`: `0.959349593495935`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7429189354062595`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
