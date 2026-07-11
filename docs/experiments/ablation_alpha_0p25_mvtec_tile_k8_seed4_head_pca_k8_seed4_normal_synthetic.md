# Run ablation_alpha_0p25_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9901324883987868`
- `auroc`: `0.9765512265512265`
- `brier`: `0.21589020344166127`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31577692556585`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019839409038297133`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6246661581695532`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
