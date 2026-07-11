# Run ablation_alpha_0p25_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9606516340829235`
- `auroc`: `0.9199775112443778`
- `brier`: `0.22722024214919775`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06359059492746999`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019399762650330861`
- `max_f1`: `0.9080459770114943`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6470449751504493`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
