# Run ablation_alpha_1p0_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9616857207829602`
- `auroc`: `0.8500199441563622`
- `brier`: `0.15209410284536026`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16689081941590167`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002729459341163888`
- `max_f1`: `0.9251101321585903`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.486401681416304`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
