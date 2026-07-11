# Run ablation_pca16_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9890833893634731`
- `auroc`: `0.9675438596491228`
- `brier`: `0.10753795441862313`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12871342423170082`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028384035288155835`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4208415131308592`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
