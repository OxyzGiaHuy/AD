# Run ablation_pca128_mvtec_wood_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.99213609933655`
- `auroc`: `0.9754385964912281`
- `brier`: `0.20317368782456596`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21698333153241794`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003970144245820709`
- `max_f1`: `0.957983193277311`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.375660676039906`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
