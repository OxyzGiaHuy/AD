# Run ablation_alpha_0p25_mvtec_transistor_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7561347525503135`
- `auroc`: `0.8033333333333333`
- `brier`: `0.2595931593305953`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15369578003883355`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003095259293913841`
- `max_f1`: `0.7291666666666666`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7123532523334667`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
