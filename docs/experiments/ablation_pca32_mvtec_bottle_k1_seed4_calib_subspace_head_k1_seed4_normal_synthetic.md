# Run ablation_pca32_mvtec_bottle_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9823889095544558`
- `auroc`: `0.953968253968254`
- `brier`: `0.22536120322573408`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2315661763570395`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002791647204613111`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.980882238824048`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
