# Run ablation_calib_upper_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9884406562428972`
- `auroc`: `0.950030284675954`
- `brier`: `0.06419310083455249`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.04403541775822056`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002028375024012491`
- `max_f1`: `0.953125`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.21383083300879877`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
