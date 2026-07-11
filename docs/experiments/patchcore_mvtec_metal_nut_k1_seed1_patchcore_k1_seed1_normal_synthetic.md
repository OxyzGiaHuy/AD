# Run patchcore_mvtec_metal_nut_k1_seed1_patchcore_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9962131890473424`
- `auroc`: `0.9833822091886608`
- `brier`: `0.19130434782608696`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19130434782608696`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005123307426338611`
- `max_f1`: `0.968421052631579`
- `model_storage_mb`: `2.00537109375`
- `nll`: `3.5239563233600646`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_metal_nut_k1_seed1_patchcore_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
