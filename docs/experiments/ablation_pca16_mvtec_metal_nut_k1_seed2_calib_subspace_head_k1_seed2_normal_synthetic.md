# Run ablation_pca16_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9628457361552208`
- `auroc`: `0.8699902248289345`
- `brier`: `0.18354033383060844`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18258524459341297`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001551452408666196`
- `max_f1`: `0.934010152284264`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8179700465718939`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
