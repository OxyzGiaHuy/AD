# Run ablation_pca128_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9584962889548203`
- `auroc`: `0.8352612684483446`
- `brier`: `0.1220964937596186`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12160993635541556`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00315793047687321`
- `max_f1`: `0.933920704845815`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6333504867917199`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
