# Run headpca_visa_candle_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/experiments/headpca_visa_candle.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.5471460327767917`
- `auroc`: `0.5123`
- `brier`: `0.24997115234282263`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0042923678457736925`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.031123095797374843`
- `max_f1`: `0.6666666666666666`
- `model_storage_mb`: `0.09668350219726562`
- `nll`: `0.6930894901811442`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/headpca_visa_candle_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
