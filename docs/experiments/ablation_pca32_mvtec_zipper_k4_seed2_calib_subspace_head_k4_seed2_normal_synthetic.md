# Run ablation_pca32_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9796655986458092`
- `auroc`: `0.928046218487395`
- `brier`: `0.13633921619780717`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15040637993420297`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003352227873656134`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.7859529685270263`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
