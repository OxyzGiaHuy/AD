# Run ablation_alpha_1p0_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9518789166117088`
- `auroc`: `0.9036731634182908`
- `brier`: `0.2501613593394656`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13114154338836673`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023270925879478456`
- `max_f1`: `0.8663101604278075`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6979730791536769`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
