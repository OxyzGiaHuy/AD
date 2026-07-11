# Run subspacead_mvtec_bottle_k8_seed3_subspacead_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9895316790070026`
- `auroc`: `0.9706349206349206`
- `brier`: `0.21448460647366546`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2213054952851261`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013227756752307157`
- `max_f1`: `0.9612403100775194`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.736235583788242`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_bottle_k8_seed3_subspacead_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
