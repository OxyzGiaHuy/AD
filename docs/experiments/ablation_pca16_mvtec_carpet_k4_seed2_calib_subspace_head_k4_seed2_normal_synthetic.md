# Run ablation_pca16_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9982357389757365`
- `auroc`: `0.9943820224719101`
- `brier`: `0.09318717614229834`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12865497929672914`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001761840911120431`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.29660330513932043`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
