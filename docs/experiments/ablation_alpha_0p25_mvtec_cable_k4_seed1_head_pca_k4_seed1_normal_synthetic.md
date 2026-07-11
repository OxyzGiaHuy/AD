# Run ablation_alpha_0p25_mvtec_cable_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9580582121090798`
- `auroc`: `0.9197901049475262`
- `brier`: `0.22899482502684387`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13633502205212905`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003085222380856673`
- `max_f1`: `0.8901734104046243`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6507650847646091`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
