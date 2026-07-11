# Run ablation_alpha_0p25_mvtec_cable_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9398851588709958`
- `auroc`: `0.8832458770614693`
- `brier`: `0.23770307085967227`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16968710819880162`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002489721414943536`
- `max_f1`: `0.8588235294117647`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6684532439100181`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
