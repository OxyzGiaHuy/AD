# Run ablation_pca64_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9143993660172387`
- `auroc`: `0.7962697274031564`
- `brier`: `0.19395399646370598`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18924548922805112`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001986226218286902`
- `max_f1`: `0.8715953307392996`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.900968723341823`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
