# Run ablation_alpha_0p25_mvtec_grid_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_grid_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9980811403508771`
- `auroc`: `0.9941520467836257`
- `brier`: `0.2166606097067076`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.39151262358213085`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003362333903519007`
- `max_f1`: `0.9911504424778761`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6262542190156705`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_grid_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
