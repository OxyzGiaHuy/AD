# Run patchcore_mvtec_zipper_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9929656318453445`
- `auroc`: `0.976890756302521`
- `brier`: `0.7657759080430345`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7685277462869093`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01248845968716192`
- `max_f1`: `0.975`
- `model_storage_mb`: `6.0`
- `nll`: `3.424244636847162`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_zipper_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
