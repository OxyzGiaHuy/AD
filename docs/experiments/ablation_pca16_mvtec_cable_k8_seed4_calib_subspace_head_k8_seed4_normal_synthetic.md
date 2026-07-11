# Run ablation_pca16_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9000651929121709`
- `auroc`: `0.8302098950524738`
- `brier`: `0.17885943768621876`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16610662673910456`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002149251823623975`
- `max_f1`: `0.8177339901477833`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5828429222943116`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
