# Run ablation_pca64_mvtec_carpet_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9974594188000838`
- `auroc`: `0.9919743178170144`
- `brier`: `0.05611943457809049`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07707534889634857`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002307707316472999`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.37712217813365995`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
