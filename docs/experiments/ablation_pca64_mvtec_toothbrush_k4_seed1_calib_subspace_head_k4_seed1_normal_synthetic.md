# Run ablation_pca64_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.989197430655764`
- `auroc`: `0.9722222222222222`
- `brier`: `0.2052048442227951`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23783988612038748`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003991936954359214`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2591871190631703`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
