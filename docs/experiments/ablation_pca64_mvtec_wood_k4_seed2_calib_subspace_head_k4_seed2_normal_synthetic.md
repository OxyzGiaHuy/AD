# Run ablation_pca64_mvtec_wood_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.981904646006159`
- `auroc`: `0.9438596491228071`
- `brier`: `0.21527996650163816`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.225283686873279`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018877347200354443`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.5911223638812877`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
