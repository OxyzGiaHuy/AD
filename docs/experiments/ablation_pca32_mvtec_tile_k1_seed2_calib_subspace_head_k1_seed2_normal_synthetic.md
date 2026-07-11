# Run ablation_pca32_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.98952988625588`
- `auroc`: `0.9743867243867244`
- `brier`: `0.27411251644992707`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27784011659459174`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013382366070380579`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.404725682321863`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
