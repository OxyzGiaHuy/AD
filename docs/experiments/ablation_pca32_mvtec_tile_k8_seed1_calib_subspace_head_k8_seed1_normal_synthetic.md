# Run ablation_pca32_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9877261162209724`
- `auroc`: `0.9696969696969697`
- `brier`: `0.11477744251469524`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14607169854844743`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0031238318954268074`
- `max_f1`: `0.9473684210526315`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.39907193872851177`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
