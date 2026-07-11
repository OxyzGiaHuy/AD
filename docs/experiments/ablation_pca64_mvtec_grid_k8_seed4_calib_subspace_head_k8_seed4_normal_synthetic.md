# Run ablation_pca64_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_grid_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.999697519661222`
- `auroc`: `0.9991645781119465`
- `brier`: `0.18131181316306783`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20294203236699102`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032796203516996824`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6928575720708503`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
