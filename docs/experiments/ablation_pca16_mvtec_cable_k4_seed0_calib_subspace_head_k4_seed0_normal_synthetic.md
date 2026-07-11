# Run ablation_pca16_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.911493903135012`
- `auroc`: `0.8532608695652174`
- `brier`: `0.3097183421527554`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3109554052352905`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001960136406123638`
- `max_f1`: `0.8272251308900523`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.9121840631727645`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
