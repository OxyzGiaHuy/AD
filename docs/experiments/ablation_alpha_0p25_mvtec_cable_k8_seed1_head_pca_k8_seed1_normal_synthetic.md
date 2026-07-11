# Run ablation_alpha_0p25_mvtec_cable_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9517427525792133`
- `auroc`: `0.9062968515742129`
- `brier`: `0.22766896055985697`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17700000921885178`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002506803385913372`
- `max_f1`: `0.8863636363636364`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6480926015238854`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
