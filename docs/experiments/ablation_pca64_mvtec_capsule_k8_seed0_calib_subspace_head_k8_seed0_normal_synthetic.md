# Run ablation_pca64_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9388635802988127`
- `auroc`: `0.7750299162345433`
- `brier`: `0.1342633689020736`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1306907107355073`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022495281882584095`
- `max_f1`: `0.9237668161434978`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.770662513699315`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
