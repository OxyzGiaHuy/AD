# Run ablation_alpha_1p0_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9752936180583324`
- `auroc`: `0.9083469721767594`
- `brier`: `0.12780368556405078`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17851715815995262`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023056347324641167`
- `max_f1`: `0.9448275862068966`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4283324651740107`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
