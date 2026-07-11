# Run ablation_pca128_mvtec_bottle_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9833756273359627`
- `auroc`: `0.9523809523809523`
- `brier`: `0.2357991434909188`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23828051535479988`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015049239463475813`
- `max_f1`: `0.943089430894309`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.685573063678295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
