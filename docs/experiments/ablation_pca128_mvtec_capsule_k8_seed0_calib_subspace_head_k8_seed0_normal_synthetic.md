# Run ablation_pca128_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.957283494195528`
- `auroc`: `0.8312724371759075`
- `brier`: `0.10754031451052058`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1064932481950206`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022290316974800644`
- `max_f1`: `0.9344978165938864`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.556846645703508`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
