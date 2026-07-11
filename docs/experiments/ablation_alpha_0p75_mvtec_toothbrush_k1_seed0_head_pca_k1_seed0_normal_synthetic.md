# Run ablation_alpha_0p75_mvtec_toothbrush_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_toothbrush_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9716901587598251`
- `auroc`: `0.9111111111111111`
- `brier`: `0.20308557224139637`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18530846493584768`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0051484063622497375`
- `max_f1`: `0.9152542372881356`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5961879564030523`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_toothbrush_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
