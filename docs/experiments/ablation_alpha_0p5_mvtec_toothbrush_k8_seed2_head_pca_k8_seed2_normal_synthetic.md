# Run ablation_alpha_0p5_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9841098303500974`
- `auroc`: `0.9583333333333334`
- `brier`: `0.20408415834969545`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17894447559402113`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004308052006221953`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5991806334236072`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
