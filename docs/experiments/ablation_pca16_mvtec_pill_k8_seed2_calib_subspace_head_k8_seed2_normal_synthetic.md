# Run ablation_pca16_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9734203420277308`
- `auroc`: `0.869885433715221`
- `brier`: `0.07582320184726853`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07147466328865046`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018073720578661936`
- `max_f1`: `0.9423728813559322`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.25090608750740795`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
