# Run ablation_pca32_mvtec_screw_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8639419510894204`
- `auroc`: `0.6771879483500718`
- `brier`: `0.22607163657375895`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20211857503454664`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030664443504065273`
- `max_f1`: `0.8634686346863468`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.9103655802463629`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
