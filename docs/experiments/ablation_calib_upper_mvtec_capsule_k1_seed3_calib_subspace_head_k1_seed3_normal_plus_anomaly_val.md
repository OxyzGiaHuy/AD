# Run ablation_calib_upper_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9561201763575616`
- `auroc`: `0.849802371541502`
- `brier`: `0.16446944602233163`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.1576474577677054`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014645648723254439`
- `max_f1`: `0.9292929292929293`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5777234076369704`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
