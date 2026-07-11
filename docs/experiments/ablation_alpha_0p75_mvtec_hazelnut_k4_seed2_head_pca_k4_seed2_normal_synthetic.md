# Run ablation_alpha_0p75_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9848463215252331`
- `auroc`: `0.9664285714285714`
- `brier`: `0.22961692801161127`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.043344237587668706`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020523878491737627`
- `max_f1`: `0.9402985074626866`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6513049558449063`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
