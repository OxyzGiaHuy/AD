# Run calib_subspace_head_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9933446187513909`
- `auroc`: `0.9726295210166178`
- `brier`: `0.1152547973517029`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12681578703872542`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013272429937901703`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7920791832573396`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
