# Run ablation_pca128_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9577252346339459`
- `auroc`: `0.9184782608695652`
- `brier`: `0.3267645897011453`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34549503087997435`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023418445015947024`
- `max_f1`: `0.88268156424581`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.4619046275625036`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
