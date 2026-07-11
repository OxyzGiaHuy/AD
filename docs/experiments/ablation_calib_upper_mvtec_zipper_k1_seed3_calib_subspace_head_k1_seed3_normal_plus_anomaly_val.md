# Run ablation_calib_upper_mvtec_zipper_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.971459344601986`
- `auroc`: `0.9105902777777778`
- `brier`: `0.17878019272163448`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.18745035954884115`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017807506024837493`
- `max_f1`: `0.9391304347826087`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5738442840719136`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
