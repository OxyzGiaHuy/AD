# Run ablation_calib_upper_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9867142177994163`
- `auroc`: `0.9600389863547758`
- `brier`: `0.15994259359774424`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.17987977743965303`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026919850441690994`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4876481932991617`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
