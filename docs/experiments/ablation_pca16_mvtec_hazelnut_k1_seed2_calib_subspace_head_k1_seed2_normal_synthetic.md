# Run ablation_pca16_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8121137966595148`
- `auroc`: `0.6964285714285714`
- `brier`: `0.3062878925776935`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3136086702315052`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003648122823373838`
- `max_f1`: `0.8`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `2.144466592125278`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
