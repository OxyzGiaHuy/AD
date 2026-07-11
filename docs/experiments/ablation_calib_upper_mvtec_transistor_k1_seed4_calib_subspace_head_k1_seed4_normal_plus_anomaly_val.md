# Run ablation_calib_upper_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7724594990351917`
- `auroc`: `0.8273148148148148`
- `brier`: `0.4075434246765452`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.4698376193021735`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025433199286150434`
- `max_f1`: `0.7111111111111111`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.3574570829626955`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
