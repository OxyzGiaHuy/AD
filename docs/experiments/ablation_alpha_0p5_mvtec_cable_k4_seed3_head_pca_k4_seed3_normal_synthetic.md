# Run ablation_alpha_0p5_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9279151292691965`
- `auroc`: `0.8682533733133433`
- `brier`: `0.2312892515500973`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.011814520756403657`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030997786670923233`
- `max_f1`: `0.8636363636363636`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6547169568382882`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
