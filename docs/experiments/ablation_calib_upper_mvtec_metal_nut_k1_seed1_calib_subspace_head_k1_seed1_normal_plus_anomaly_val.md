# Run ablation_calib_upper_mvtec_metal_nut_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9949784456246376`
- `auroc`: `0.9805194805194806`
- `brier`: `0.14898787477359135`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.1658047954991179`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001489640898861975`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.466111787859765`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
