# Run ablation_alpha_0p5_mvtec_capsule_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9720455249556882`
- `auroc`: `0.8811328280813722`
- `brier`: `0.1705758290826289`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2354661569450841`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0038722471305818267`
- `max_f1`: `0.9298245614035088`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5297227001831029`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
