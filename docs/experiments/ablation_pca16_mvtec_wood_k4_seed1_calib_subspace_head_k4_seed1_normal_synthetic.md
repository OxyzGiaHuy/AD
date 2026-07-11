# Run ablation_pca16_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9921533007035808`
- `auroc`: `0.9763157894736842`
- `brier`: `0.15895608200188444`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17717995650217513`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002045847074706343`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.47157071787091254`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
