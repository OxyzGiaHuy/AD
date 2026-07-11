# Run ablation_pca32_mvtec_screw_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7950521992591684`
- `auroc`: `0.5824964131994261`
- `brier`: `0.24466854069802163`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23325189562747256`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018456530291587115`
- `max_f1`: `0.855072463768116`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.34503241099413`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
