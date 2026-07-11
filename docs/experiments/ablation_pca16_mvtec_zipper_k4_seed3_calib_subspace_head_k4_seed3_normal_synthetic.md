# Run ablation_pca16_mvtec_zipper_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9685044322098826`
- `auroc`: `0.898109243697479`
- `brier`: `0.08914695297105266`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09642389936130558`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001450973285349789`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5333538488756294`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
