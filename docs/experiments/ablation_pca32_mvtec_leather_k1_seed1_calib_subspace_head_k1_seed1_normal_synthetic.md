# Run ablation_pca32_mvtec_leather_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_leather_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.21718853424151244`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23201331183795001`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013644219856829413`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.4035273282794123`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_leather_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
