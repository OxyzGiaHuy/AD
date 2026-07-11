# Run ablation_pca32_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9855310567676977`
- `auroc`: `0.9293507910529187`
- `brier`: `0.08900455654598781`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09485481676651153`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002077070828861819`
- `max_f1`: `0.9491525423728814`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4233605273464271`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
