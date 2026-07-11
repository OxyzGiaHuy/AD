# Run patchcore_mvtec_screw_k1_seed3_patchcore_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.8181598650176971`
- `auroc`: `0.6566919450707112`
- `brier`: `0.25625`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25625`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005077055736910552`
- `max_f1`: `0.8686131386861314`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.720299446787697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k1_seed3_patchcore_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
