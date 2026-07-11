# Run ablation_pca32_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7989021467227844`
- `auroc`: `0.6148800983808157`
- `brier`: `0.2542203535062678`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25515609495341784`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019545091199688613`
- `max_f1`: `0.8717948717948718`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.3202476162098984`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
