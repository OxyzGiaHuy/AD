# Run ablation_calib_upper_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9845507801918627`
- `auroc`: `0.9354936402180497`
- `brier`: `0.0673800592514446`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.06624993813388487`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021597891924233217`
- `max_f1`: `0.9618320610687023`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.23128696379910954`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
