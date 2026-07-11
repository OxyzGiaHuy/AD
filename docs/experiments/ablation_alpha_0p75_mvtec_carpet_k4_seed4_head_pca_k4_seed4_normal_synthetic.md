# Run ablation_alpha_0p75_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9826832977622914`
- `auroc`: `0.9382022471910112`
- `brier`: `0.16071576600519513`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27652125175182635`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002568410996061105`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5052152709528739`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
