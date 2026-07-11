# Run ablation_calib_upper_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.985097555653501`
- `auroc`: `0.9448051948051948`
- `brier`: `0.10762289456771995`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.1169216933677781`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002662004498800017`
- `max_f1`: `0.9431818181818182`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3352947723308372`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
