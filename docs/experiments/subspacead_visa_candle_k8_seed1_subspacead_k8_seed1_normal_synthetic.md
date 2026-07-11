# Run subspacead_visa_candle_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/subspacead_visa_candle_k8_seed1.yaml`
- Dataset: `visa`
- Model: `subspacead`

## Metrics

- `ap`: `0.8645716220103745`
- `auroc`: `0.8842`
- `brier`: `0.48561348442361024`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4912089791893959`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.007922304347157478`
- `max_f1`: `0.8348623853211009`
- `model_storage_mb`: `0.09521484375`
- `nll`: `2.2954996134894605`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_visa_candle_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
