# Run ablation_pca128_mvtec_bottle_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9968415599228934`
- `auroc`: `0.9904761904761905`
- `brier`: `0.1856929053920439`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2046239995453731`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027788213442966163`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8626861224679736`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
