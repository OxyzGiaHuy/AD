# Run ablation_pca32_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9395581851035074`
- `auroc`: `0.8817466266866567`
- `brier`: `0.2917848829752066`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.305937872727712`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0031040637691815694`
- `max_f1`: `0.8651685393258427`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.8405205792281144`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
