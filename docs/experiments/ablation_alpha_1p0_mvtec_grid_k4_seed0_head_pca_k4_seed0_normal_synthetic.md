# Run ablation_alpha_1p0_mvtec_grid_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9863465566518022`
- `auroc`: `0.9640768588137009`
- `brier`: `0.19152842758490174`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04586093013103196`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.005276691908828723`
- `max_f1`: `0.9565217391304348`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5688012961142129`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
