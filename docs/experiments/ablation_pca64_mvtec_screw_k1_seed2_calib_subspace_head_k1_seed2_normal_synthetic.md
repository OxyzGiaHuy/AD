# Run ablation_pca64_mvtec_screw_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7703676600227763`
- `auroc`: `0.5650748104119697`
- `brier`: `0.25039469825073896`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2526840824633837`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020675999694503844`
- `max_f1`: `0.8603773584905661`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `3.210157650087134`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
