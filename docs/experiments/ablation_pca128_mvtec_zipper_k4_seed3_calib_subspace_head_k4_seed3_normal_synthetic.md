# Run ablation_pca128_mvtec_zipper_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.980274355223936`
- `auroc`: `0.9311974789915967`
- `brier`: `0.1313297418095019`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15312544797972732`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022815095125049943`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6513868492341687`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
