# Run ablation_pca128_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9730807907951982`
- `auroc`: `0.9361111111111111`
- `brier`: `0.2855246250949576`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28561918650354656`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003999736559178148`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.175350458710934`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
