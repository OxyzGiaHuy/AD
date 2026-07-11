# Run ablation_pca128_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9972720022773277`
- `auroc`: `0.9882697947214076`
- `brier`: `0.11020597076468965`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13345433227393932`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002934912559778794`
- `max_f1`: `0.978494623655914`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5159232383995925`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
