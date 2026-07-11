# Run ablation_alpha_0p0_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9893947914168759`
- `auroc`: `0.9701754385964912`
- `brier`: `0.2601579238353083`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2970679315585124`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0033086365253864962`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7133945059602258`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
