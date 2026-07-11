# Run ablation_pca128_mvtec_wood_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.989864368805672`
- `auroc`: `0.968421052631579`
- `brier`: `0.13775724474475096`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16236715245095992`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025805027896090398`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8893686378661886`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
