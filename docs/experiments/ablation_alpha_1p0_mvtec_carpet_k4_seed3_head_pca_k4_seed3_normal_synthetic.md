# Run ablation_alpha_1p0_mvtec_carpet_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9922642167673815`
- `auroc`: `0.9735152487961477`
- `brier`: `0.15267558485344934`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27021605489600414`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027193263905425356`
- `max_f1`: `0.9534883720930233`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.482937225917357`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
