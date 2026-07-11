# Run ablation_pca16_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9978565616997027`
- `auroc`: `0.9931781701444623`
- `brier`: `0.1654746116033919`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1436846057573954`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020283851931747207`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5275309755672404`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
