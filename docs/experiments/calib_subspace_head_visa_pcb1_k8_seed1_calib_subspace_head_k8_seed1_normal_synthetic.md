# Run calib_subspace_head_visa_pcb1_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/calib_subspace_head_visa_pcb1_k8_seed1.yaml`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7851304552849157`
- `auroc`: `0.7895`
- `brier`: `0.24826704232151342`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23370846260746475`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002798085184767842`
- `max_f1`: `0.7636363636363637`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2219696929194042`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_visa_pcb1_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
