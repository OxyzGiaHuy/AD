# Run ablation_pca32_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9178976656890214`
- `auroc`: `0.731551655364978`
- `brier`: `0.11264878751336181`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07835875936981407`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020907768189455524`
- `max_f1`: `0.9224137931034483`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3655296394675376`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
