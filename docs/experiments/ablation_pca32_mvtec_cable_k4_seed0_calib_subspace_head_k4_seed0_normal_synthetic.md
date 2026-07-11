# Run ablation_pca32_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9404793652897819`
- `auroc`: `0.8888680659670165`
- `brier`: `0.298100867530104`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31724004705746967`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013377446308732034`
- `max_f1`: `0.8633879781420765`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.9103757634586053`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
