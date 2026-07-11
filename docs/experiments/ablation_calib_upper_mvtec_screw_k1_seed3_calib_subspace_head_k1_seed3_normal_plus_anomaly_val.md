# Run ablation_calib_upper_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.729515093137291`
- `auroc`: `0.5103884372177055`
- `brier`: `0.2670306066133694`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.2688512422094409`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002456640837176534`
- `max_f1`: `0.8404669260700389`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.4271030025040854`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
