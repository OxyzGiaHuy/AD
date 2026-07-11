# Run ablation_alpha_0p75_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9639390032192128`
- `auroc`: `0.9241004497751124`
- `brier`: `0.23202974364348108`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3129644211133321`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00347337432205677`
- `max_f1`: `0.9080459770114943`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6556264567722239`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
