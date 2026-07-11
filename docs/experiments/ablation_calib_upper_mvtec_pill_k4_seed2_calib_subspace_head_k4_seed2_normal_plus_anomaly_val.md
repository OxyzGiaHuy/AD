# Run ablation_calib_upper_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9845253067792341`
- `auroc`: `0.9336765596608116`
- `brier`: `0.08324598424802963`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.0723955133576799`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020658526496559965`
- `max_f1`: `0.9538461538461539`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.26831620609620915`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
