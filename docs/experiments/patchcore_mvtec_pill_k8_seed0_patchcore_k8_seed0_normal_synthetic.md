# Run patchcore_mvtec_pill_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9844190908541643`
- `auroc`: `0.9298963447899619`
- `brier`: `0.7883468443930894`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8077056644718625`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012598699360282834`
- `max_f1`: `0.9543859649122807`
- `model_storage_mb`: `6.0`
- `nll`: `2.8855995602248554`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_pill_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
