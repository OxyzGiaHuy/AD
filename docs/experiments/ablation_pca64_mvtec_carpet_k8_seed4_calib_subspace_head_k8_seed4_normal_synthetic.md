# Run ablation_pca64_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9991484148226796`
- `auroc`: `0.9971910112359551`
- `brier`: `0.04747107959145783`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06792633868033779`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002646668822082699`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.13541883544447908`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
