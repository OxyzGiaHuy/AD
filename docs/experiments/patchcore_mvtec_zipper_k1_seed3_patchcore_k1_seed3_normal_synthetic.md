# Run patchcore_mvtec_zipper_k1_seed3_patchcore_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_zipper_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.994468225089621`
- `auroc`: `0.9779411764705882`
- `brier`: `0.2119205298013245`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21192052980132448`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005033706802110009`
- `max_f1`: `0.9704641350210971`
- `model_storage_mb`: `2.00537109375`
- `nll`: `3.9037204293753867`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_zipper_k1_seed3_patchcore_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
