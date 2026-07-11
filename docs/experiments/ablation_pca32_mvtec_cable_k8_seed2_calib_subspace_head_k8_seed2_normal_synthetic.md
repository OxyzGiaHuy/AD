# Run ablation_pca32_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9522695193283903`
- `auroc`: `0.9072338830584707`
- `brier`: `0.23151592766619483`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24724041730165477`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002745253841082255`
- `max_f1`: `0.8876404494382022`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6521964645066232`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
