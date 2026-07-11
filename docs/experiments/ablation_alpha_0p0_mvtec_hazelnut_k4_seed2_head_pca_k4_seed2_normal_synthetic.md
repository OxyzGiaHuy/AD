# Run ablation_alpha_0p0_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9895618267290313`
- `auroc`: `0.9810714285714286`
- `brier`: `0.24120465430254695`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3439086569981141`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003472496907819401`
- `max_f1`: `0.9395973154362416`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6755203494187316`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
