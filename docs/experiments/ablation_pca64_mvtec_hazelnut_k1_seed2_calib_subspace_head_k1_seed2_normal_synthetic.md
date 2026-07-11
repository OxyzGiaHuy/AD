# Run ablation_pca64_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9149754115228349`
- `auroc`: `0.8625`
- `brier`: `0.36362610021580066`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36363038529049263`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001833390173586932`
- `max_f1`: `0.8551724137931035`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.869304684424951`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
