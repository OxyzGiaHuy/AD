# Run ablation_alpha_1p0_mvtec_leather_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9983586765339288`
- `auroc`: `0.9949048913043478`
- `brier`: `0.16255188365234186`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31573170087029856`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018587250172370864`
- `max_f1`: `0.9891304347826086`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.500880012136274`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
