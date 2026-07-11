# Run ablation_pca16_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9005462673842302`
- `auroc`: `0.6820901475867571`
- `brier`: `0.13350158460712075`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08286578157408674`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017255111033040466`
- `max_f1`: `0.9210526315789473`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.43679822937249474`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
