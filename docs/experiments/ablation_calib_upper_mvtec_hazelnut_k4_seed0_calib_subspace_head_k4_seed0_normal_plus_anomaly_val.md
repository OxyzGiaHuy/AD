# Run ablation_calib_upper_mvtec_hazelnut_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.970516189041443`
- `auroc`: `0.9531746031746032`
- `brier`: `0.24722724439212232`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.2940034438105463`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004254831218169731`
- `max_f1`: `0.9130434782608695`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7690665492510714`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
