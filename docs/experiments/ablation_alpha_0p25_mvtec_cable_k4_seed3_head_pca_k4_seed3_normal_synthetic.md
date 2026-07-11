# Run ablation_alpha_0p25_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9274403792068335`
- `auroc`: `0.8686281859070465`
- `brier`: `0.23249186238713118`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08074222167332971`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0034406046817700067`
- `max_f1`: `0.8539325842696629`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.657851138410896`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
