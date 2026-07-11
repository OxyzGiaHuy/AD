# Run ablation_alpha_1p0_mvtec_grid_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9901123015425313`
- `auroc`: `0.9741019214703425`
- `brier`: `0.18638354626070125`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16820014592928767`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017683888093019144`
- `max_f1`: `0.957983193277311`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5575710187193575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
