# Run ablation_pca128_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9992631940604584`
- `auroc`: `0.9975922953451043`
- `brier`: `0.06517920989087514`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08944830747369009`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002516790874238707`
- `max_f1`: `0.9886363636363636`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.382588807236647`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
