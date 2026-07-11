# Run ablation_alpha_1p0_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9866908053850584`
- `auroc`: `0.9660894660894661`
- `brier`: `0.1793311872303003`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17485557509283728`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025372372414821233`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5374105203357424`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
