# Run ablation_pca64_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9998751560549313`
- `auroc`: `0.9995987158908507`
- `brier`: `0.052759711682846766`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08583731850227108`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021224246225041202`
- `max_f1`: `0.994413407821229`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.1511263408561192`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
