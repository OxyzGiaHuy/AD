# Run ablation_pca64_mvtec_carpet_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9992505332590388`
- `auroc`: `0.9975922953451043`
- `brier`: `0.20430021580083846`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21887626963802892`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002303108779920472`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2162336490615697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
