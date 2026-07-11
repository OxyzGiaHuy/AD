# Run ablation_pca32_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9636764745958519`
- `auroc`: `0.8729227761485826`
- `brier`: `0.12266127560733446`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1319768760085066`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002255032373511273`
- `max_f1`: `0.9435897435897436`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.8021117935330992`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
