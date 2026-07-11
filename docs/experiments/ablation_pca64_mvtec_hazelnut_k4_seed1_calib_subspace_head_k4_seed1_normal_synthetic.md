# Run ablation_pca64_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9893558604020432`
- `auroc`: `0.9810714285714286`
- `brier`: `0.3391773809762552`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35016547820784827`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015955073420297016`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.0980946853119438`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
