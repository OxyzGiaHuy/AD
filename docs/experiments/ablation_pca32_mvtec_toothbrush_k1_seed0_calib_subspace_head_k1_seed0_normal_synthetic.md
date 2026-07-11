# Run ablation_pca32_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9779274889545561`
- `auroc`: `0.9416666666666667`
- `brier`: `0.21768821881254766`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23668256579410463`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037083106470249946`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.9615712972283692`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
