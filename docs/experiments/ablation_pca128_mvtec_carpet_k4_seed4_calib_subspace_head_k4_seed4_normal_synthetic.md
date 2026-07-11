# Run ablation_pca128_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9997530559328313`
- `auroc`: `0.9991974317817014`
- `brier`: `0.06569999970787824`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10503679396122953`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002305087529950672`
- `max_f1`: `0.9943502824858758`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.1950841320950485`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
