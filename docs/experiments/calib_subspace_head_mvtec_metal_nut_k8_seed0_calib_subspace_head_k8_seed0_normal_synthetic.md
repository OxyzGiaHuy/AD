# Run calib_subspace_head_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9895741836733822`
- `auroc`: `0.958455522971652`
- `brier`: `0.0925429117740704`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10332146603715318`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013024822525356126`
- `max_f1`: `0.9533678756476683`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5833714509957876`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
