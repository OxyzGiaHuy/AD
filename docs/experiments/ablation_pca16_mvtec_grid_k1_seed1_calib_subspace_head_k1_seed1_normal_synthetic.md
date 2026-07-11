# Run ablation_pca16_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9656916901778383`
- `auroc`: `0.9214703425229741`
- `brier`: `0.2448111205697957`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22362059049117267`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0035703442990779877`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8398519327051247`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
