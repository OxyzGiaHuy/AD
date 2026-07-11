# Run ablation_alpha_0p5_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9965585940645307`
- `auroc`: `0.9896825396825397`
- `brier`: `0.19010874533313318`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3702575352536627`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024809999817825227`
- `max_f1`: `0.9841269841269841`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5710716004929538`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
