# Run anomalydino_mvtec_tile_k2_seed1_anomalydino_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9966829975519561`
- `auroc`: `0.9917027417027418`
- `brier`: `0.28205128205128205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28205128205128205`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008745660352655966`
- `max_f1`: `0.9822485207100592`
- `model_storage_mb`: `4.0107421875`
- `nll`: `5.195576625851375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k2_seed1_anomalydino_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
