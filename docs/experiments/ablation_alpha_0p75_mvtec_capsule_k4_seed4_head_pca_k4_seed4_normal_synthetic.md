# Run ablation_alpha_0p75_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9692665406226756`
- `auroc`: `0.8707618667730355`
- `brier`: `0.1619749216548362`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2094074189662934`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002284719382948948`
- `max_f1`: `0.918918918918919`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5100733780398681`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
