# Run ablation_alpha_0p75_mvtec_metal_nut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9876238097096038`
- `auroc`: `0.958455522971652`
- `brier`: `0.1575857941517438`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24868323232816614`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023503036278745403`
- `max_f1`: `0.972972972972973`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4991330819640321`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
