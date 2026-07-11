# Run ablation_alpha_0p75_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9900240556153874`
- `auroc`: `0.9590834697217676`
- `brier`: `0.13954217499735946`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24887604949003211`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002566611818121579`
- `max_f1`: `0.968421052631579`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4597894267572346`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
