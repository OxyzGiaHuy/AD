# Run ablation_pca64_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9856437359240282`
- `auroc`: `0.9342607746863066`
- `brier`: `0.08446810715954321`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09247766159095624`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002076598085061519`
- `max_f1`: `0.958041958041958`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.47464263991220407`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
