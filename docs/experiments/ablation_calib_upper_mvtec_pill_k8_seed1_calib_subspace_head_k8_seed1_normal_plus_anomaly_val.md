# Run ablation_calib_upper_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9869927032602072`
- `auroc`: `0.9466989703210176`
- `brier`: `0.05652685063909878`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.06112751102963699`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002256879899529071`
- `max_f1`: `0.9575289575289575`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.19966301913135157`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
