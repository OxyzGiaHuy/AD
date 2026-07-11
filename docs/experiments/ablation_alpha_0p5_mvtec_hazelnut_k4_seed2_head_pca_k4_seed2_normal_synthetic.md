# Run ablation_alpha_0p5_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.990447262486213`
- `auroc`: `0.9785714285714285`
- `brier`: `0.22421252814593684`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.007699282602830371`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001989064518023621`
- `max_f1`: `0.9583333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6401052508073232`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
