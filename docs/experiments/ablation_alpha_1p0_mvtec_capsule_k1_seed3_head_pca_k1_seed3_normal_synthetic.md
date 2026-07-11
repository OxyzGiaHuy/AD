# Run ablation_alpha_1p0_mvtec_capsule_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8779144598131818`
- `auroc`: `0.6126844834463502`
- `brier`: `0.1551147209028344`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11273622557972415`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001983261370862072`
- `max_f1`: `0.9083333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4930858614829661`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
