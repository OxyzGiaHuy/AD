# Run ablation_pca128_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9892277967101447`
- `auroc`: `0.947354064375341`
- `brier`: `0.06326213941663728`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06594667895724944`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014206993722630117`
- `max_f1`: `0.9616724738675958`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.26187367108417375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
