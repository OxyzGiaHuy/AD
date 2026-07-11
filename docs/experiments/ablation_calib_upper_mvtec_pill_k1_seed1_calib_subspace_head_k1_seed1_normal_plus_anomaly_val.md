# Run ablation_calib_upper_mvtec_pill_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9823896000714881`
- `auroc`: `0.9276196244700182`
- `brier`: `0.11864410405545521`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.12266959435020391`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001465269613986701`
- `max_f1`: `0.9578544061302682`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.38116413455981984`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
