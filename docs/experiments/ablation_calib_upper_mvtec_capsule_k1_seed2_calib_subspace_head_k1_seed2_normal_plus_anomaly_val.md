# Run ablation_calib_upper_mvtec_capsule_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9272213415099791`
- `auroc`: `0.7610891523935002`
- `brier`: `0.14655017411611576`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.13954869792109623`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014471840266077245`
- `max_f1`: `0.9107981220657277`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.555569752597106`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
