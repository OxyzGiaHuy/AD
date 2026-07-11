# Run ablation_alpha_0p5_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9917165824580065`
- `auroc`: `0.98`
- `brier`: `0.22115980319631498`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08202178532427007`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026370384307070212`
- `max_f1`: `0.9705882352941176`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6337652267249311`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
