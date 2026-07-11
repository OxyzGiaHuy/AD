# Run ablation_pca32_mvtec_bottle_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9823889095544558`
- `auroc`: `0.953968253968254`
- `brier`: `0.21575777027843104`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22427687802946708`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027403004961200506`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.2564942114032758`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
