# Run ablation_pca32_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.745751495066663`
- `auroc`: `0.47038327526132406`
- `brier`: `0.2563265306986478`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2569199163466692`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014794254093430936`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `4.377245015192598`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
