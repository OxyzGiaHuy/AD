# Run ablation_calib_upper_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9456118477047514`
- `auroc`: `0.904445367677607`
- `brier`: `0.2581737314956125`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.28784777340314066`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030299845739459315`
- `max_f1`: `0.8805031446540881`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7054125799057932`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
