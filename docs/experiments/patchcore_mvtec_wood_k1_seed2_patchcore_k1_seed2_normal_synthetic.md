# Run patchcore_mvtec_wood_k1_seed2_patchcore_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_wood_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9918936006990161`
- `auroc`: `0.9728070175438597`
- `brier`: `0.24050632911392406`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.240506329113924`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004710664265329325`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.430290311893983`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_wood_k1_seed2_patchcore_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
