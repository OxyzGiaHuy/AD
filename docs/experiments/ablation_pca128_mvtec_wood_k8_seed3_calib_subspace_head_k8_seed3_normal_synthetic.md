# Run ablation_pca128_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9918317362522463`
- `auroc`: `0.974561403508772`
- `brier`: `0.11837231627181995`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13982996172448503`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014988822225905673`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7907987752256531`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
