# Run ablation_pca128_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7469197451225795`
- `auroc`: `0.5242877638860423`
- `brier`: `0.25621899772071366`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2561508815735578`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0036753604421392084`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.0512689783750018`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
