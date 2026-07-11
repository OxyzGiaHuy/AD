# Run ablation_pca128_mvtec_toothbrush_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9698993408988801`
- `auroc`: `0.9277777777777778`
- `brier`: `0.2321679093271493`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24944738050301868`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001593880887542452`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.1277919174970337`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
