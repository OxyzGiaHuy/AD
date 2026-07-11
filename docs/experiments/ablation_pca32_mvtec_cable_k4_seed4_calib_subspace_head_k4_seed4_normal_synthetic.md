# Run ablation_pca32_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9383173334956146`
- `auroc`: `0.882496251874063`
- `brier`: `0.2776231127089344`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3040653536096215`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014972198382019997`
- `max_f1`: `0.8538011695906432`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.246253893333936`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
