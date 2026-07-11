# Run ablation_pca32_mvtec_toothbrush_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9898368114362738`
- `auroc`: `0.975`
- `brier`: `0.22422246245448912`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24013613093466984`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004212222549886931`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6813878303450893`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
