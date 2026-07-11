# Run ablation_pca128_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9687857039797539`
- `auroc`: `0.9138888888888889`
- `brier`: `0.28510251172650347`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28540637379600886`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0036698435211465472`
- `max_f1`: `0.8955223880597015`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.1530807049473872`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
