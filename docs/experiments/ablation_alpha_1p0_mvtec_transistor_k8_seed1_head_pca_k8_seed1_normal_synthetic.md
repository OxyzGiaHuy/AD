# Run ablation_alpha_1p0_mvtec_transistor_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8955046342842957`
- `auroc`: `0.9208333333333333`
- `brier`: `0.32450223527243255`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31913698017597203`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003155824448913336`
- `max_f1`: `0.8333333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8536628316143825`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
