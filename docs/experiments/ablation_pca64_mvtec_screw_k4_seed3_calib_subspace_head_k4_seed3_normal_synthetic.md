# Run ablation_pca64_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8719180259137462`
- `auroc`: `0.7526132404181185`
- `brier`: `0.17053297298523845`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1382176118117059`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001962471252772957`
- `max_f1`: `0.8784313725490196`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6953599526081795`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
