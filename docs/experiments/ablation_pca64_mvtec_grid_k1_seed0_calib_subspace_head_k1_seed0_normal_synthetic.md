# Run ablation_pca64_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9846803503966466`
- `auroc`: `0.9598997493734336`
- `brier`: `0.26909103608678103`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2691607146691054`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014297037074963252`
- `max_f1`: `0.9421487603305785`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.101686489200901`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
