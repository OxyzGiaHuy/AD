# Run ablation_alpha_0p25_mvtec_cable_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8935987562391522`
- `auroc`: `0.816904047976012`
- `brier`: `0.2369345438065298`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06160190900166829`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026525409643848737`
- `max_f1`: `0.8`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6668649028421605`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
