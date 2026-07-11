# Run patchcore_visa_candle_k8_seed2_patchcore_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_candle_k8_seed2.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.8744815368242417`
- `auroc`: `0.9013`
- `brier`: `0.4805296246072007`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47274945056065915`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.10206128903664649`
- `max_f1`: `0.8514851485148515`
- `model_storage_mb`: `6.0`
- `nll`: `1.988516342747821`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_candle_k8_seed2_patchcore_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
