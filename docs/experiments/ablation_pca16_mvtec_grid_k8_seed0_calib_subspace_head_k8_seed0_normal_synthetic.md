# Run ablation_pca16_mvtec_grid_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8917994154342538`
- `auroc`: `0.746031746031746`
- `brier`: `0.2166079889468829`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19454332498403695`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022817204873531293`
- `max_f1`: `0.8818897637795275`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6625119364246168`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
