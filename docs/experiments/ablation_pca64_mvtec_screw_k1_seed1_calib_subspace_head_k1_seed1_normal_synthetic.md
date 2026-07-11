# Run ablation_pca64_mvtec_screw_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8236425417775428`
- `auroc`: `0.6001229760196761`
- `brier`: `0.25624992400758384`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25624968148767946`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020075191278010607`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.424636507791957`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
