# Run ablation_pca64_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9126123146117624`
- `auroc`: `0.9316666666666666`
- `brier`: `0.16032008639237832`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20249345202464608`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014117979258298874`
- `max_f1`: `0.8533333333333334`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5540241685483952`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
