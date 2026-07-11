# Run ablation_alpha_1p0_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9634572491165625`
- `auroc`: `0.9138888888888889`
- `brier`: `0.1900463049036655`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07287880920228502`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002159948194665568`
- `max_f1`: `0.9354838709677419`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5628997761096185`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
