# Run ablation_alpha_0p25_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9869222063542329`
- `auroc`: `0.9356246590289143`
- `brier`: `0.20331690041167405`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3362804742273457`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001734290606604365`
- `max_f1`: `0.9466192170818505`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5991558052569189`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
