# Run ablation_pca64_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9862487192389863`
- `auroc`: `0.9666666666666667`
- `brier`: `0.1399309136202031`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17072298909936634`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0038975285632269724`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6592668577277072`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
