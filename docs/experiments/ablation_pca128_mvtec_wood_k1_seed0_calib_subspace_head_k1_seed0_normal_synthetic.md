# Run ablation_pca128_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9815427704400297`
- `auroc`: `0.9438596491228071`
- `brier`: `0.23948549485637827`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23999140911464445`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002794372389399553`
- `max_f1`: `0.9448818897637795`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.9940484243542715`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
