# Run ablation_pca32_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9846669979303262`
- `auroc`: `0.9710714285714286`
- `brier`: `0.3636363603852015`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636363620107824`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0033850874921137635`
- `max_f1`: `0.9343065693430657`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `6.672213359663157`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
