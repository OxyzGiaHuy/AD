# Run ablation_pca32_mvtec_wood_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9595875366070812`
- `auroc`: `0.8947368421052632`
- `brier`: `0.23998419017934966`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2402440181261376`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0030344272433202478`
- `max_f1`: `0.9365079365079365`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.3048948337020922`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
