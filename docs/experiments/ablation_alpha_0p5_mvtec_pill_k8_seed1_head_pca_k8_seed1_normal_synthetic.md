# Run ablation_alpha_0p5_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.990467383240365`
- `auroc`: `0.9601745771958538`
- `brier`: `0.16713879342928437`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33752657053713303`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025616234090335356`
- `max_f1`: `0.974910394265233`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5234181085505892`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
