# Run ablation_alpha_1p0_mvtec_toothbrush_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9814639482381419`
- `auroc`: `0.95`
- `brier`: `0.20148329256717148`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.037420041504360416`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005375218577682972`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5914633299712223`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
