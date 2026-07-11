# Run ablation_alpha_0p5_mvtec_wood_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9962715389185978`
- `auroc`: `0.9868421052631579`
- `brier`: `0.19213610697720132`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22457279736482638`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003400643980955776`
- `max_f1`: `0.9830508474576272`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5746077352908818`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_wood_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
