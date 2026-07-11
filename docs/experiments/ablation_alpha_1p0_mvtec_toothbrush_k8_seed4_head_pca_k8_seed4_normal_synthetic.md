# Run ablation_alpha_1p0_mvtec_toothbrush_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9826668663517886`
- `auroc`: `0.9555555555555556`
- `brier`: `0.2006394544967763`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0675182385104044`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020980695706038248`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.589514908163042`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
