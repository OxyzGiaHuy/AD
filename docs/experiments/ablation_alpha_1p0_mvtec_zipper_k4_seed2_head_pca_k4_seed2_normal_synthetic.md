# Run ablation_alpha_1p0_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.982942169063304`
- `auroc`: `0.9406512605042017`
- `brier`: `0.15643690464517984`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14974886652649644`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002518190663085868`
- `max_f1`: `0.9435483870967742`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.490325516144282`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
