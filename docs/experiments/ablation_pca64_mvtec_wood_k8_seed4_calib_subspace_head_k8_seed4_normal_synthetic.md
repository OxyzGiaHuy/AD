# Run ablation_pca64_mvtec_wood_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9893947914168759`
- `auroc`: `0.9701754385964912`
- `brier`: `0.11103929836691379`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12816763495955663`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002703258366901663`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1980094567076331`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
