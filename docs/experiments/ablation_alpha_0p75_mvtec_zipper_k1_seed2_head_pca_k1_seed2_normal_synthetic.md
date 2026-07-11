# Run ablation_alpha_0p75_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9828718163070297`
- `auroc`: `0.9380252100840336`
- `brier`: `0.17645620190038241`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27346484076897826`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022282083919703565`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.540532049241414`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
