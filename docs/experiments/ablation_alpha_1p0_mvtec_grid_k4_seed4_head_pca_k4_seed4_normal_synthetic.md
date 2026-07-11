# Run ablation_alpha_1p0_mvtec_grid_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9578961119914837`
- `auroc`: `0.8939014202172096`
- `brier`: `0.18839930626354914`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11525395665413302`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028197204407591084`
- `max_f1`: `0.9193548387096774`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5622795875968295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
