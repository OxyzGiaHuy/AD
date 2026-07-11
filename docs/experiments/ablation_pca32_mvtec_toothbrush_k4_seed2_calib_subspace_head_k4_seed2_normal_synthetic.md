# Run ablation_pca32_mvtec_toothbrush_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9841679795356975`
- `auroc`: `0.9611111111111111`
- `brier`: `0.14382100758619099`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16517470759295289`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0038052681567413466`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.8929462768895345`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
