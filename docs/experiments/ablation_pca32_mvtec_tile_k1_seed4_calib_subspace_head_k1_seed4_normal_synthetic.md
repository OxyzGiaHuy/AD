# Run ablation_pca32_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.992655220911912`
- `auroc`: `0.9823232323232324`
- `brier`: `0.20726906942514167`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2228400715856621`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003746144441712616`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.9966098570321338`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
