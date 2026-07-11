# Run ablation_pca64_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9779400349531113`
- `auroc`: `0.9222873900293255`
- `brier`: `0.12860681959447193`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14295325182054353`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021950224009544953`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7021492420717997`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
