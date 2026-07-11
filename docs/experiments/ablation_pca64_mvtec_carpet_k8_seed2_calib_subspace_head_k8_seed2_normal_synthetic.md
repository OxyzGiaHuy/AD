# Run ablation_pca64_mvtec_carpet_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9990107006884094`
- `auroc`: `0.9967897271268058`
- `brier`: `0.21814844873605166`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2955181621787194`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002196382030717328`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6751743752867789`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
