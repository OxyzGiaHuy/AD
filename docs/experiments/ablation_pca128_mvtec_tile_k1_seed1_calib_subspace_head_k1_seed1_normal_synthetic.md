# Run ablation_pca128_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.996709940172795`
- `auroc`: `0.9917027417027418`
- `brier`: `0.25842095136835574`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26953455831250583`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017551156477286266`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.07027365715356`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
