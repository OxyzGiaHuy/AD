# Run patchcore_mvtec_toothbrush_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9676806945510149`
- `auroc`: `0.9305555555555556`
- `brier`: `0.6959234893662788`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.696466028357723`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012106594851329214`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `6.0`
- `nll`: `3.130353389483603`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_toothbrush_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
