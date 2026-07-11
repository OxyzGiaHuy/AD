# Run ablation_alpha_0p0_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9856437359240282`
- `auroc`: `0.9342607746863066`
- `brier`: `0.2452158364627531`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.41459410579618583`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023606110386505813`
- `max_f1`: `0.958041958041958`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6835635245853025`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
