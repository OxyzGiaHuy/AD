# Run ablation_alpha_1p0_mvtec_wood_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9895973262915615`
- `auroc`: `0.9754385964912281`
- `brier`: `0.180040595064681`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15088730145104326`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020744708614258826`
- `max_f1`: `0.9833333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5451995548420001`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
