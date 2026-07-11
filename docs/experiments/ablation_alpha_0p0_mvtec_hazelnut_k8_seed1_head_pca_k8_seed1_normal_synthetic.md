# Run ablation_alpha_0p0_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9952928635184961`
- `auroc`: `0.9917857142857143`
- `brier`: `0.23735152549690505`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13710224574262445`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002451619268818335`
- `max_f1`: `0.9722222222222222`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6678351209515861`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
