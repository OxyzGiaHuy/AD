# Run ablation_pca32_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9773070729720711`
- `auroc`: `0.9416666666666667`
- `brier`: `0.2546138695959473`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2661144811482656`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015870505234315282`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.0393522677421987`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
