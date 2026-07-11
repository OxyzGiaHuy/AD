# Run ablation_pca64_mvtec_zipper_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9732151223993105`
- `auroc`: `0.9078256302521008`
- `brier`: `0.20564473308316408`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20860913770877765`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020161355346046536`
- `max_f1`: `0.9402390438247012`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.581030200917666`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
