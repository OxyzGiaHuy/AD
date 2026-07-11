# Run ablation_alpha_0p5_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.923681707049494`
- `auroc`: `0.8607571214392804`
- `brier`: `0.2338130378196261`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0014347545305888332`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002135128217438857`
- `max_f1`: `0.8297872340425532`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6601743544635172`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
