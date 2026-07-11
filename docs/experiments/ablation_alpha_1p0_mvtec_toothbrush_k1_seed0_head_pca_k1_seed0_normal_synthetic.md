# Run ablation_alpha_1p0_mvtec_toothbrush_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9427214932308773`
- `auroc`: `0.7986111111111112`
- `brier`: `0.20287667160331924`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.003567810569490737`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003430766763076896`
- `max_f1`: `0.8709677419354839`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5953767801686987`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
