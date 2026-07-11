# Run ablation_pca64_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9328021472131383`
- `auroc`: `0.8808095952023988`
- `brier`: `0.3865564402064287`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3866071697076162`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026663946732878685`
- `max_f1`: `0.8415841584158416`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.340234556981457`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
