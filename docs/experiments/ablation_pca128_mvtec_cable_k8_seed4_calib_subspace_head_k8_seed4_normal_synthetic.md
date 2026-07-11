# Run ablation_pca128_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9532534087893375`
- `auroc`: `0.9055472263868066`
- `brier`: `0.24644108750447088`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27475728265941146`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002382141314446926`
- `max_f1`: `0.8953488372093024`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.9488693554276801`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
