# Run ablation_alpha_0p5_mvtec_leather_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_leather_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9998831229546516`
- `auroc`: `0.9996603260869565`
- `brier`: `0.1834463161007758`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.41461109874709956`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0039978916155955484`
- `max_f1`: `0.9945945945945946`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5570069992527408`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_leather_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
