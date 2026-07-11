# Run ablation_pca16_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_leather_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9942384195364495`
- `auroc`: `0.9833559782608695`
- `brier`: `0.19045863840442437`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20248587498621587`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017910552541575125`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `2.3910118945560677`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
