# Run ablation_pca64_mvtec_bottle_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9847970574021614`
- `auroc`: `0.957936507936508`
- `brier`: `0.23784153801195765`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23932337473673992`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003023222470319415`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.1598874956087593`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_bottle_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
