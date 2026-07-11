# Run ablation_calib_upper_mvtec_wood_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9866806631111091`
- `auroc`: `0.9658869395711501`
- `brier`: `0.16400526021767228`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.192558033417349`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022158584978482494`
- `max_f1`: `0.9629629629629629`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.567186304994974`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
