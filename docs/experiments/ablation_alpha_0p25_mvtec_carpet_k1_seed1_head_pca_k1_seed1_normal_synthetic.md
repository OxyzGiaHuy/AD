# Run ablation_alpha_0p25_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_carpet_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9941454404504511`
- `auroc`: `0.9803370786516854`
- `brier`: `0.2080978146915558`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.37891735098300827`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002974621378458463`
- `max_f1`: `0.9550561797752809`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6089084601996757`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
