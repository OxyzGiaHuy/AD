# Run ablation_pca16_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7342076795813064`
- `auroc`: `0.7975`
- `brier`: `0.2978924691128467`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34693479500710966`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014027870446443559`
- `max_f1`: `0.6888888888888889`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.9495330678723807`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
