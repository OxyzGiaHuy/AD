# Run ablation_calib_upper_mvtec_bottle_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9932203529263739`
- `auroc`: `0.9824561403508771`
- `brier`: `0.06777707286425094`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.10318767172949657`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025682030850416654`
- `max_f1`: `0.9743589743589743`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.251062871395498`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
