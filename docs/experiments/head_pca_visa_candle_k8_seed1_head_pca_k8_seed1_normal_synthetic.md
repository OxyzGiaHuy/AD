# Run head_pca_visa_candle_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8645716220103745`
- `auroc`: `0.8842`
- `brier`: `0.2321472495435522`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16802260488271714`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0034644944593310357`
- `max_f1`: `0.8348623853211009`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6573617920640095`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
