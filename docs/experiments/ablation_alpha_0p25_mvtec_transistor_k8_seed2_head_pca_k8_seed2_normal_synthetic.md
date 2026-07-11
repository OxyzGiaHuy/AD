# Run ablation_alpha_0p25_mvtec_transistor_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8715571394255527`
- `auroc`: `0.9041666666666667`
- `brier`: `0.24598851855398698`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16670179933309553`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0027275418676435946`
- `max_f1`: `0.8043478260869565`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6849530772163765`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
