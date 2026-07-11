# Run patchcore_mvtec_bottle_k1_seed3_patchcore_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.983482280586615`
- `auroc`: `0.9611111111111111`
- `brier`: `0.24096385542168675`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24096385542168675`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0038706957171839402`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.438718257934363`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_bottle_k1_seed3_patchcore_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
