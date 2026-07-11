# Run anomalydino_visa_macaroni2_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_macaroni2_k8_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8038594152785643`
- `auroc`: `0.7935`
- `brier`: `0.4797550984975469`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4754379457654431`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09631419976241887`
- `max_f1`: `0.7549019607843137`
- `model_storage_mb`: `6.0`
- `nll`: `1.9768794122023374`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_macaroni2_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
