# Run ablation_pca128_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9956247416800087`
- `auroc`: `0.98989898989899`
- `brier`: `0.09363450197553438`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12427339505436075`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022183859991466897`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.36296337211669755`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
