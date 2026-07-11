# Run ablation_calib_upper_mvtec_screw_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8992810078033309`
- `auroc`: `0.7915537488708221`
- `brier`: `0.18138028664170303`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.1858425198080669`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002048829795430171`
- `max_f1`: `0.8727272727272727`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7315579731692475`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
