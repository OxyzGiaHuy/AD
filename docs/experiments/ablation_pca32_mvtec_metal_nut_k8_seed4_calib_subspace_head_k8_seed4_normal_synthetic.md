# Run ablation_pca32_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9616079297746228`
- `auroc`: `0.8748778103616813`
- `brier`: `0.1171646665326061`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12647993992204248`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015009640999462293`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4838282881355131`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
