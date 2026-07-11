# Run calib_subspace_head_mvtec_metal_nut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.998442758557556`
- `auroc`: `0.9931573802541545`
- `brier`: `0.05807338880263291`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07897643706882777`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012860168743392695`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.19938027158910424`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_metal_nut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
