# Run ablation_alpha_0p25_mvtec_carpet_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_carpet_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9988757132041219`
- `auroc`: `0.9963884430176565`
- `brier`: `0.20084088197071592`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.41183304914042485`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003074535447308141`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5942847841018136`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_carpet_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
