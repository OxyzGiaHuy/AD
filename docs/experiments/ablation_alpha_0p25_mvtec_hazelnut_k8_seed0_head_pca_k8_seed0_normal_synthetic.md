# Run ablation_alpha_0p25_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9870401420894415`
- `auroc`: `0.9735714285714285`
- `brier`: `0.22569989989108635`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1267062387683175`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002419247952374545`
- `max_f1`: `0.948905109489051`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.644124814930606`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
