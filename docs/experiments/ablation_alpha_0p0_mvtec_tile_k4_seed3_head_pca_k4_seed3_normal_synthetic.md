# Run ablation_alpha_0p0_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9952906419907501`
- `auroc`: `0.9891774891774892`
- `brier`: `0.2667590246118779`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3378355859691261`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003039113476745084`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7265316107359543`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
