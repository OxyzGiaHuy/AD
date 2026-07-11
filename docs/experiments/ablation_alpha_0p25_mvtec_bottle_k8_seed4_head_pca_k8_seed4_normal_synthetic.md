# Run ablation_alpha_0p25_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9967916942976308`
- `auroc`: `0.9904761904761905`
- `brier`: `0.21187807933638064`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.42029632071414624`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003413643867495548`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.616542000737978`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
