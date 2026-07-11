# Run ablation_calib_upper_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9900863609522684`
- `auroc`: `0.9780701754385965`
- `brier`: `0.05676821527557563`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.09614181053747825`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014844488591775982`
- `max_f1`: `0.9673202614379085`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.22145318170450798`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
