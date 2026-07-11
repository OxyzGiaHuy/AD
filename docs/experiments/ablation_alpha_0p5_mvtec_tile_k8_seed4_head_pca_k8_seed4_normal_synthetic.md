# Run ablation_alpha_0p5_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9891321589016965`
- `auroc`: `0.974025974025974`
- `brier`: `0.19629574998554328`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35528356524614185`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002548436244201456`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5834962568917572`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
