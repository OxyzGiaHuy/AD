# Run patchcore_mvtec_tile_k2_seed0_patchcore_k2_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k2_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9934815156838985`
- `auroc`: `0.9848484848484849`
- `brier`: `0.28205128205128205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28205128205128205`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008575703837295882`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `4.0107421875`
- `nll`: `5.195576625851375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k2_seed0_patchcore_k2_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
