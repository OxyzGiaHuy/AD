# Run patchcore_mvtec_cable_k8_seed4_patchcore_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.954135445533694`
- `auroc`: `0.9102323838080959`
- `brier`: `0.5736698759010046`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5739156562214096`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012411587250729402`
- `max_f1`: `0.8727272727272727`
- `model_storage_mb`: `6.0`
- `nll`: `2.119553188411938`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_cable_k8_seed4_patchcore_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
