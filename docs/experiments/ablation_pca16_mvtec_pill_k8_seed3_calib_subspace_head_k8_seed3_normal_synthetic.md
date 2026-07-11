# Run ablation_pca16_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9739481886755483`
- `auroc`: `0.8742498636115658`
- `brier`: `0.07841943992805732`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07302912020453523`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013636997315341127`
- `max_f1`: `0.9463087248322147`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.29604509572522913`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
