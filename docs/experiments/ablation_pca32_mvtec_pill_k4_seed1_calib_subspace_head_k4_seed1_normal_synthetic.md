# Run ablation_pca32_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9762555519368599`
- `auroc`: `0.8881614839061648`
- `brier`: `0.1272524636141329`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12165334160456394`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022374521606339666`
- `max_f1`: `0.9355932203389831`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.47684878104377093`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
