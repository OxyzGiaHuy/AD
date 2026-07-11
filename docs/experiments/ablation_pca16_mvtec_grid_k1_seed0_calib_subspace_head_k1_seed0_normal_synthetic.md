# Run ablation_pca16_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9120989784956106`
- `auroc`: `0.7953216374269005`
- `brier`: `0.26923052164344013`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692306454365071`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0032168586189166093`
- `max_f1`: `0.8888888888888888`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `4.8713019403430575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
