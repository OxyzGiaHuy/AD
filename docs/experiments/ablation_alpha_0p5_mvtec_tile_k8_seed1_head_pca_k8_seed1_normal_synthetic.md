# Run ablation_alpha_0p5_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9877415889969554`
- `auroc`: `0.9689754689754689`
- `brier`: `0.19527261007738717`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2813746631145477`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029658451517168274`
- `max_f1`: `0.9647058823529412`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.581631243439557`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
