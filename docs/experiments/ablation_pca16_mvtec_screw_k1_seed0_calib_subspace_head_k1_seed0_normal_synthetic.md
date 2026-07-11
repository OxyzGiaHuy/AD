# Run ablation_pca16_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7991467730875492`
- `auroc`: `0.5538020086083214`
- `brier`: `0.24898267273604077`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22816432978579543`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016323111718520521`
- `max_f1`: `0.8561151079136691`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.9301719693926873`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
