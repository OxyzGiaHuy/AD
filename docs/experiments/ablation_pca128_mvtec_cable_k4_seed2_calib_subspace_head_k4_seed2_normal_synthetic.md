# Run ablation_pca128_mvtec_cable_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9558879480061515`
- `auroc`: `0.9134182908545727`
- `brier`: `0.3240443491451067`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.343137425382932`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020451655983924864`
- `max_f1`: `0.88268156424581`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.4293563613785374`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
