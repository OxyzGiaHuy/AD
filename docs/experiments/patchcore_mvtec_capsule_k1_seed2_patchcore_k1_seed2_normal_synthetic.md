# Run patchcore_mvtec_capsule_k1_seed2_patchcore_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9577460007249787`
- `auroc`: `0.8201037096130833`
- `brier`: `0.17424242424242425`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1742424242424242`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005047837512172533`
- `max_f1`: `0.9083333333333333`
- `model_storage_mb`: `2.00537109375`
- `nll`: `3.2096640764040534`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_capsule_k1_seed2_patchcore_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
