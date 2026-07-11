# Run ablation_alpha_0p75_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8984659736684162`
- `auroc`: `0.7673703627792581`
- `brier`: `0.19214804904074487`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0866705164313316`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002673357632011175`
- `max_f1`: `0.8702290076335878`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5731007637267485`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
