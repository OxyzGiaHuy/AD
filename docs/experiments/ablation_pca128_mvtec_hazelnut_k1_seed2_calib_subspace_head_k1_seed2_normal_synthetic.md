# Run ablation_pca128_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.919788603952067`
- `auroc`: `0.865`
- `brier`: `0.3635004252625561`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3635564278472554`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015338259833780202`
- `max_f1`: `0.8611111111111112`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.6195373485162516`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
