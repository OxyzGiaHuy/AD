# Run ablation_alpha_1p0_mvtec_transistor_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.6452697188667201`
- `auroc`: `0.653125`
- `brier`: `0.3466421034561138`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32654480040073397`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024757347628474235`
- `max_f1`: `0.6122448979591837`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.9057791918718732`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
