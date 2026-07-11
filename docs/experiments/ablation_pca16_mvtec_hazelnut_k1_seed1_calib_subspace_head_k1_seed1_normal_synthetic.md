# Run ablation_pca16_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9683112736957376`
- `auroc`: `0.9417857142857143`
- `brier`: `0.3615426173618874`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36257206309925427`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017673031850294633`
- `max_f1`: `0.9076923076923077`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `3.6966160091917946`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
