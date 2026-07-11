# Run ablation_alpha_0p25_mvtec_hazelnut_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9916312912647272`
- `auroc`: `0.9814285714285714`
- `brier`: `0.23293639119833393`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08525263450362464`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018729464235630903`
- `max_f1`: `0.9710144927536232`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6588284502204502`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
