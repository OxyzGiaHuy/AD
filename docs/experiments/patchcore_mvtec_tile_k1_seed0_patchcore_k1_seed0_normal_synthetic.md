# Run patchcore_mvtec_tile_k1_seed0_patchcore_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9938316136355393`
- `auroc`: `0.9855699855699855`
- `brier`: `0.28205128205128205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28205128205128205`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003851186181617598`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `2.00537109375`
- `nll`: `5.195576625851375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k1_seed0_patchcore_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
