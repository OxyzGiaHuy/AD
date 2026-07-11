# Run ablation_alpha_0p25_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9720447082877042`
- `auroc`: `0.8907060231352214`
- `brier`: `0.20509981208721142`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29235172587813757`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024015925062650986`
- `max_f1`: `0.935064935064935`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6027256663606729`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
