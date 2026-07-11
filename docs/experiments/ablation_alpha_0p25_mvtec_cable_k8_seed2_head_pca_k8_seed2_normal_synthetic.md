# Run ablation_alpha_0p25_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9625558025993561`
- `auroc`: `0.9212893553223388`
- `brier`: `0.22666846600398907`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11528087377548218`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023141072566310564`
- `max_f1`: `0.9195402298850575`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6460150958186781`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
