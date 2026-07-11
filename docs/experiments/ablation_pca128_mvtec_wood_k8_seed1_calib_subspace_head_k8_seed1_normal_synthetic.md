# Run ablation_pca128_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9867594637033007`
- `auroc`: `0.9614035087719298`
- `brier`: `0.14085285548491794`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1644061210600636`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002297163834866089`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8926820780261148`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
