# Run ablation_pca16_mvtec_zipper_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9840693015991047`
- `auroc`: `0.9438025210084033`
- `brier`: `0.1029830911228488`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.122098943934042`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002621060891064587`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5879180374097349`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
