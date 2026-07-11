# Run ablation_pca32_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8809770071178599`
- `auroc`: `0.7335519573683131`
- `brier`: `0.17379658978219195`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11351820211857562`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025019401218742132`
- `max_f1`: `0.8603773584905661`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5305963553975017`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
