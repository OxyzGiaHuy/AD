# Run ablation_pca128_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9869638601514272`
- `auroc`: `0.956140350877193`
- `brier`: `0.24019585883628344`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2403466241269171`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0028828929968272585`
- `max_f1`: `0.9344262295081968`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.3145510781942646`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
