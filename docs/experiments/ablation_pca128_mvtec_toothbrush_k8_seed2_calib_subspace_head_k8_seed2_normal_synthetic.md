# Run ablation_pca128_mvtec_toothbrush_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9863949680519017`
- `auroc`: `0.9666666666666667`
- `brier`: `0.13262713021324876`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1570519467460968`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00243756937838736`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7815661310493159`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
