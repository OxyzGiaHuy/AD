# Run ablation_calib_upper_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9884152728527325`
- `auroc`: `0.9707602339181286`
- `brier`: `0.083813787372265`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.11623556539416315`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026839501288247435`
- `max_f1`: `0.9724770642201835`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3069008535682368`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
