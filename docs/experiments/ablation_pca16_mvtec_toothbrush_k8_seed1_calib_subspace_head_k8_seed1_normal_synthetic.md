# Run ablation_pca16_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9794497728567066`
- `auroc`: `0.9472222222222222`
- `brier`: `0.08750942853826099`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12972368619271687`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0034612667791190602`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.29935181494091323`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
