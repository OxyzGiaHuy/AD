# Run calib_subspace_head_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9964121218496904`
- `auroc`: `0.9913419913419913`
- `brier`: `0.26244254510574494`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27149502843873125`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013043858174584869`
- `max_f1`: `0.9822485207100592`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.3599798105245664`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
