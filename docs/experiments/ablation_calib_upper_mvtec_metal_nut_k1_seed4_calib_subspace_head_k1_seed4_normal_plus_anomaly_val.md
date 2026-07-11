# Run ablation_calib_upper_mvtec_metal_nut_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9906275235908869`
- `auroc`: `0.9637445887445888`
- `brier`: `0.10165681274131665`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.11582634541785942`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0032874281114002443`
- `max_f1`: `0.9479768786127167`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3322793575860613`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
