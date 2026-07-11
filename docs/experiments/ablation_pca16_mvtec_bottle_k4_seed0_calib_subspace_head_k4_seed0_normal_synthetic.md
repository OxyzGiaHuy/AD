# Run ablation_pca16_mvtec_bottle_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9455908100239871`
- `auroc`: `0.8992063492063492`
- `brier`: `0.06696526641522765`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06456618349864539`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0032112355826489896`
- `max_f1`: `0.9465648854961832`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2518385915082368`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
