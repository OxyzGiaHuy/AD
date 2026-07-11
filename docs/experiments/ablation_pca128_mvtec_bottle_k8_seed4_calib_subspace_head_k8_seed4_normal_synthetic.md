# Run ablation_pca128_mvtec_bottle_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967064757924635`
- `auroc`: `0.9896825396825397`
- `brier`: `0.14272815883240728`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16474351183657193`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017479640622454953`
- `max_f1`: `0.9763779527559056`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6368588233662879`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
