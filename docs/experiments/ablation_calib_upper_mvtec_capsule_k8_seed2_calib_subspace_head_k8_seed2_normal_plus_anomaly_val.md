# Run ablation_calib_upper_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9712874141735645`
- `auroc`: `0.8972332015810277`
- `brier`: `0.09874772200298813`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.09110858659336313`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020352752085347646`
- `max_f1`: `0.9353233830845771`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.34954780427850973`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
