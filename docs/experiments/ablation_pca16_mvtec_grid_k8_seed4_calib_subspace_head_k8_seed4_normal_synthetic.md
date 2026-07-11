# Run ablation_pca16_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.896269171919538`
- `auroc`: `0.7602339181286549`
- `brier`: `0.17791500369691401`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16821062369033307`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002927743232785127`
- `max_f1`: `0.8852459016393442`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5461505128217722`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
