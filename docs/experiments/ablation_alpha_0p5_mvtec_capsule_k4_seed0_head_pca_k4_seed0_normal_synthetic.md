# Run ablation_alpha_0p5_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.956054334441577`
- `auroc`: `0.8340646190666134`
- `brier`: `0.17372184447105268`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23568721341364315`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002056185212550741`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5366545823582459`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
