# Run ablation_pca32_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.986851165636769`
- `auroc`: `0.9318057828696127`
- `brier`: `0.07785599681476242`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08209134539983842`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019181229977193706`
- `max_f1`: `0.9395973154362416`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.28994025060830036`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
