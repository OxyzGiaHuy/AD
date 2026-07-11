# Run ablation_alpha_0p25_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9926748129564709`
- `auroc`: `0.9825`
- `brier`: `0.2242390538988725`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13483647108078003`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003106646459888328`
- `max_f1`: `0.9714285714285714`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6411461820196417`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
