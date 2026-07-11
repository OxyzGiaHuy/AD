# Run ablation_alpha_0p0_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9740000173260935`
- `auroc`: `0.8847227762265656`
- `brier`: `0.2446966392133521`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33224346849954495`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019368338116416426`
- `max_f1`: `0.9344978165938864`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6825259798710523`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
