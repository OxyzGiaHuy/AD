# Run ablation_pca128_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9102640650827373`
- `auroc`: `0.8454469507101086`
- `brier`: `0.2688535900230442`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26904044930751514`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027496741177179874`
- `max_f1`: `0.926829268292683`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.9786406629534903`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
