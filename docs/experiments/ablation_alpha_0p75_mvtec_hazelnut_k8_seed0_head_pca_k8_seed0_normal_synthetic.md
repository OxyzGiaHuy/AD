# Run ablation_alpha_0p75_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9892185930348413`
- `auroc`: `0.9785714285714285`
- `brier`: `0.22787214800152045`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05808095173402266`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0037725259803912856`
- `max_f1`: `0.965034965034965`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6470849520812902`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
