# Run ablation_pca16_mvtec_grid_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9748473992979275`
- `auroc`: `0.9331662489557226`
- `brier`: `0.2601647930460704`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26335683465003973`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0029189961795241404`
- `max_f1`: `0.9217391304347826`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `4.30136140665421`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
