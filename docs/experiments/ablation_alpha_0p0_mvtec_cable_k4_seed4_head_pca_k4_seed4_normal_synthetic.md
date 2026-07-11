# Run ablation_alpha_0p0_mvtec_cable_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9504683633717075`
- `auroc`: `0.8978635682158921`
- `brier`: `0.24261719103968696`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.167521910071373`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002643750011920929`
- `max_f1`: `0.8888888888888888`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6783649397507016`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
