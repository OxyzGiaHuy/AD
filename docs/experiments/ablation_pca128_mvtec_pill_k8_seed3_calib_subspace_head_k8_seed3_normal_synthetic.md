# Run ablation_pca128_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9889007054150182`
- `auroc`: `0.9495362793235134`
- `brier`: `0.0604227218126432`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06892522223974148`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001846751209326133`
- `max_f1`: `0.9608540925266904`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.23420190781119718`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
