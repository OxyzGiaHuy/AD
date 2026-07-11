# Run ablation_alpha_0p75_mvtec_carpet_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9791027161319232`
- `auroc`: `0.9213483146067416`
- `brier`: `0.18115730918311798`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3114036795420524`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019177253970987776`
- `max_f1`: `0.9239766081871345`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.54965287730194`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
