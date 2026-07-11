# Run ablation_alpha_0p25_mvtec_tile_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9948387110755063`
- `auroc`: `0.9884559884559885`
- `brier`: `0.21820710756484082`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32587539360054535`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028003895989595316`
- `max_f1`: `0.9882352941176471`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6293881997874399`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
