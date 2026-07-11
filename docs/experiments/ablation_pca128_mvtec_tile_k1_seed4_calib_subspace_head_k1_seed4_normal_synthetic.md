# Run ablation_pca128_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9960213755017707`
- `auroc`: `0.9902597402597403`
- `brier`: `0.2529584091510526`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26638651760215437`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001567171822883125`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0093600041846003`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
