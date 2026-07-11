# Run ablation_pca128_mvtec_wood_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9942202864082671`
- `auroc`: `0.9824561403508771`
- `brier`: `0.23959953101341613`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24005027888696395`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027421052225782903`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.1150753174652124`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
