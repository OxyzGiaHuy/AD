# Run patchcore_mvtec_cable_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.950276091614259`
- `auroc`: `0.9061094452773614`
- `brier`: `0.6071627692587808`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6057803718474072`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.011872561785082022`
- `max_f1`: `0.861878453038674`
- `model_storage_mb`: `6.0`
- `nll`: `3.3634059855746483`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_cable_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
