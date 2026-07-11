# Run ablation_pca16_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9775920995833276`
- `auroc`: `0.9388888888888889`
- `brier`: `0.11012082065217424`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1287165894949188`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0027885567396879196`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3738387428618669`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
