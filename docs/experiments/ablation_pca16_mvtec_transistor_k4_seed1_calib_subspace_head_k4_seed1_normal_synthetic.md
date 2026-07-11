# Run ablation_pca16_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7227297999069047`
- `auroc`: `0.8016666666666666`
- `brier`: `0.22158888554985803`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22810715031555445`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025643825717270373`
- `max_f1`: `0.7083333333333334`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8190316038851523`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
