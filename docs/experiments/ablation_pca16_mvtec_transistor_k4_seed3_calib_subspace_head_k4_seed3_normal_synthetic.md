# Run ablation_pca16_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7319532158288696`
- `auroc`: `0.7970833333333334`
- `brier`: `0.25850777283093707`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.268791832147399`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002587589491158724`
- `max_f1`: `0.7010309278350515`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.1302466836407492`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
