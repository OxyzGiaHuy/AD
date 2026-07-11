# Run ablation_pca64_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9858217488906953`
- `auroc`: `0.9707142857142858`
- `brier`: `0.3636323745494105`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636343527923931`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0040052249011668295`
- `max_f1`: `0.9496402877697842`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `5.226054681280666`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
