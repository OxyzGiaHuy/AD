# Run ablation_pca16_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9906040452087107`
- `auroc`: `0.9692982456140351`
- `brier`: `0.19474205337297276`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21223554316955273`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002593625124685372`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.0000701749464125`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
