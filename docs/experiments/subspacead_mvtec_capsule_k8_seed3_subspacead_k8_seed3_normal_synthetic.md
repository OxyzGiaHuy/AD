# Run subspacead_mvtec_capsule_k8_seed3_subspacead_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9435474181617609`
- `auroc`: `0.7989629038691664`
- `brier`: `0.17230370589306493`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17221508107402106`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012560158431755774`
- `max_f1`: `0.933920704845815`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.0138465587562442`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_capsule_k8_seed3_subspacead_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
