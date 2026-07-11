# Run ablation_pca16_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9576000092365656`
- `auroc`: `0.9126984126984127`
- `brier`: `0.10210674674864409`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11124452731027885`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018291792282498027`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5029055432543424`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
