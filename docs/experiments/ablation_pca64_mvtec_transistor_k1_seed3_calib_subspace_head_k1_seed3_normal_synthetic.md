# Run ablation_pca64_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8002312251767195`
- `auroc`: `0.8370833333333333`
- `brier`: `0.5979590903761351`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5989571225643158`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025119582004845143`
- `max_f1`: `0.7346938775510204`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `7.2028674111929085`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
