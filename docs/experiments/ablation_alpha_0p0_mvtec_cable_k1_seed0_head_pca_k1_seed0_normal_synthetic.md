# Run ablation_alpha_0p0_mvtec_cable_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.949356378922941`
- `auroc`: `0.8969265367316341`
- `brier`: `0.24578094881935447`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12294390320777887`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025053079922993976`
- `max_f1`: `0.8757396449704142`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6847048996226542`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
