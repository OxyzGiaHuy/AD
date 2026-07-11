# Run ablation_pca32_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9997530559328313`
- `auroc`: `0.9991974317817014`
- `brier`: `0.024344236028840713`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.03886402316558633`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002608330156176518`
- `max_f1`: `0.9943502824858758`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.08057755178605348`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
