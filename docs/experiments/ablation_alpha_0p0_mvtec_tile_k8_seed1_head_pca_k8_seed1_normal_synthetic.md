# Run ablation_alpha_0p0_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9898483790983981`
- `auroc`: `0.9758297258297258`
- `brier`: `0.2770345095381672`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3382604180747627`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005472859845329554`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7471441528402956`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
