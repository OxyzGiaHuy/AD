# Run ablation_alpha_0p0_mvtec_carpet_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_carpet_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9991484148226796`
- `auroc`: `0.9971910112359551`
- `brier`: `0.2551791808074809`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4697028688895397`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0031407326300684204`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7030171056790553`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_carpet_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
