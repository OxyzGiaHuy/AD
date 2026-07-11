# Run ablation_pca64_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_cable_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9504683633717075`
- `auroc`: `0.8978635682158921`
- `brier`: `0.34552971578057917`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35796958933273954`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001970380221803983`
- `max_f1`: `0.8888888888888888`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.8530174422104604`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
