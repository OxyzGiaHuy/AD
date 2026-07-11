# Run ablation_pca16_mvtec_hazelnut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9183605671899754`
- `auroc`: `0.8560714285714286`
- `brier`: `0.3170366593006196`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3093347858298909`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002160226604477926`
- `max_f1`: `0.8607594936708861`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.0144210143217482`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
