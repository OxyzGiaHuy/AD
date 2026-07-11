# Run ablation_alpha_0p25_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9906374372629749`
- `auroc`: `0.9604473540643753`
- `brier`: `0.20034865468920737`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3833644791634497`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022529993362412483`
- `max_f1`: `0.9750889679715302`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5931518847637176`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
