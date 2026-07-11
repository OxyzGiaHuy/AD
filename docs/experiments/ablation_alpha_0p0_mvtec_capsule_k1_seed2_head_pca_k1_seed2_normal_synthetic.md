# Run ablation_alpha_0p0_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9351214015359111`
- `auroc`: `0.7682489030714`
- `brier`: `0.24134707321752474`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31738035177642654`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003359212243760174`
- `max_f1`: `0.9184549356223176`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6758289155315917`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
