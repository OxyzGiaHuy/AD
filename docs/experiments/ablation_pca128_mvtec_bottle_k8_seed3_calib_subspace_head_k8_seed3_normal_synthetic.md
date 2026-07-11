# Run ablation_pca128_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9925253658582068`
- `auroc`: `0.9785714285714285`
- `brier`: `0.14065638224173047`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16647629868463587`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00304708010460957`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.628919676737013`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
