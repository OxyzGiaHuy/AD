# Run anomalydino_mvtec_tile_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9948629633542412`
- `auroc`: `0.9884559884559885`
- `brier`: `0.7129359067810292`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7092658702341808`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012912308080838276`
- `max_f1`: `0.9822485207100592`
- `model_storage_mb`: `6.0`
- `nll`: `4.244419979395948`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
