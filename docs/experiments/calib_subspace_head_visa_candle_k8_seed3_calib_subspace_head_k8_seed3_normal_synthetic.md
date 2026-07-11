# Run calib_subspace_head_visa_candle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/calib_subspace_head_visa_candle_k8_seed3.yaml`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8521831860345257`
- `auroc`: `0.8818`
- `brier`: `0.19352222652594972`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18993551298161032`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.006164417443796992`
- `max_f1`: `0.8272727272727273`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.9045400440289518`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_visa_candle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
