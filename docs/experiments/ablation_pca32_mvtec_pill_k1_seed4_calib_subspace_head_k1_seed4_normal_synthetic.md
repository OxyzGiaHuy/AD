# Run ablation_pca32_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9679211651708376`
- `auroc`: `0.845608292416803`
- `brier`: `0.1450280085149554`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14702795365613386`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00195974390396101`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.929414636082175`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
