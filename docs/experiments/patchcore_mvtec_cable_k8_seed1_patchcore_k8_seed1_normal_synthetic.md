# Run patchcore_mvtec_cable_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_cable_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.951962557725765`
- `auroc`: `0.9081709145427287`
- `brier`: `0.5925430855425419`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5911741576498994`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012597526386380196`
- `max_f1`: `0.8817204301075269`
- `model_storage_mb`: `6.0`
- `nll`: `2.5424167467202743`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_cable_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
