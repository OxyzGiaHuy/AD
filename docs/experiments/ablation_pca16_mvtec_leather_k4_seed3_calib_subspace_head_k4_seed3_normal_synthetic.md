# Run ablation_pca16_mvtec_leather_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_leather_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9948551609740501`
- `auroc`: `0.9847146739130435`
- `brier`: `0.09034986118625529`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10868393961760785`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018673948192548368`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2942728814371869`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_leather_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
