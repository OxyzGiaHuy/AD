# Run ablation_alpha_1p0_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9234005147200278`
- `auroc`: `0.8560714285714286`
- `brier`: `0.24033623564304726`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.104444755749269`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025676008144562895`
- `max_f1`: `0.8363636363636363`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6768971195873319`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
