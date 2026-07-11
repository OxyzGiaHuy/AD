# Run ablation_alpha_0p75_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9560125759279895`
- `auroc`: `0.83047467092142`
- `brier`: `0.15364365266584518`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1933988513368549`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0029720851417743797`
- `max_f1`: `0.9210526315789473`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.49070372589827416`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
