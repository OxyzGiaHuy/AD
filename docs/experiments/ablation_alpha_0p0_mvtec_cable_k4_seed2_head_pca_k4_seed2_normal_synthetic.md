# Run ablation_alpha_0p0_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9564891279381816`
- `auroc`: `0.9137931034482759`
- `brier`: `0.23847930079378102`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22102445046106978`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0033235817402601244`
- `max_f1`: `0.8901734104046243`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6700798731489342`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
