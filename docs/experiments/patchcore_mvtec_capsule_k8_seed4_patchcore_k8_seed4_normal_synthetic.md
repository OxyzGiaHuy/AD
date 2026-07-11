# Run patchcore_mvtec_capsule_k8_seed4_patchcore_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9786275476565652`
- `auroc`: `0.908256880733945`
- `brier`: `0.5329276038288844`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6270721350429637`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012369158762422476`
- `max_f1`: `0.9417040358744395`
- `model_storage_mb`: `6.0`
- `nll`: `1.3603454023831656`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_capsule_k8_seed4_patchcore_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
