# Run ablation_pca64_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_capsule_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9606937181678282`
- `auroc`: `0.8496210610291185`
- `brier`: `0.17353093388929194`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17365965337464295`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026036820825979566`
- `max_f1`: `0.9308755760368663`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.7077433280245948`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
