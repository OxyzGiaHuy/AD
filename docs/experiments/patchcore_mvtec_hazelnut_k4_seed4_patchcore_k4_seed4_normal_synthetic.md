# Run patchcore_mvtec_hazelnut_k4_seed4_patchcore_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9916478272295828`
- `auroc`: `0.9857142857142858`
- `brier`: `0.6311742845076392`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6305945349740796`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012299241311848164`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `6.0`
- `nll`: `3.535470882870533`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_hazelnut_k4_seed4_patchcore_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
