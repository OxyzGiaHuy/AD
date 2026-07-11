# Run ablation_pca16_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9995073634751871`
- `auroc`: `0.9983948635634029`
- `brier`: `0.08184901704591166`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13619421877794796`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016611875950271247`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.25391371957897163`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
