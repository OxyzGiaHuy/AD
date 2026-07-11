# Run ablation_alpha_1p0_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9978994029057829`
- `auroc`: `0.9926470588235294`
- `brier`: `0.14422788506279444`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29035677736168664`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005155701881015538`
- `max_f1`: `0.9873417721518988`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4634107876230638`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
