# Run ablation_calib_upper_mvtec_screw_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8118944109966015`
- `auroc`: `0.6011743450767841`
- `brier`: `0.2673142966615577`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.2643719695558483`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001671775750465841`
- `max_f1`: `0.8404669260700389`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2780140374178692`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
