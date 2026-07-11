# Run ablation_alpha_1p0_mvtec_metal_nut_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.977219580744309`
- `auroc`: `0.9022482893450635`
- `brier`: `0.16364010046640742`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1026330496953881`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026564336665298627`
- `max_f1`: `0.9292929292929293`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.511867549574955`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
