# Run ablation_alpha_1p0_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9616364542022974`
- `auroc`: `0.9182908545727136`
- `brier`: `0.24359760086075274`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11054078737894697`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024825885022679963`
- `max_f1`: `0.9080459770114943`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6816523203568228`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
