# Run head_pca_visa_candle_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8713067057939664`
- `auroc`: `0.8837`
- `brier`: `0.2296985817927954`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19933782875537873`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030753278732299806`
- `max_f1`: `0.8415841584158416`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6524170065090076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
