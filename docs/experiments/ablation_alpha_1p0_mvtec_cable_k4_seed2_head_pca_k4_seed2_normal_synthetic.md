# Run ablation_alpha_1p0_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9330353625201322`
- `auroc`: `0.8680659670164917`
- `brier`: `0.2515499996392334`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12689292629559837`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024743589386343958`
- `max_f1`: `0.8395061728395061`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7014233226597744`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
