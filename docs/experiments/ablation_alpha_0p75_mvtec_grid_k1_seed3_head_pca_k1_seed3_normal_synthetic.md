# Run ablation_alpha_0p75_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9314450545312319`
- `auroc`: `0.8061821219715957`
- `brier`: `0.20373902919306353`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08937686146833956`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0030709910325897047`
- `max_f1`: `0.85`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5984722096611678`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
