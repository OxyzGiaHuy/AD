# Run ablation_pca16_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9523911086867166`
- `auroc`: `0.9063492063492063`
- `brier`: `0.09969988390819477`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12578601933207856`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003917179238724421`
- `max_f1`: `0.9393939393939394`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.31344598871922164`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
