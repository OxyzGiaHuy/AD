# Run ablation_pca16_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9466998344278289`
- `auroc`: `0.8992063492063492`
- `brier`: `0.08349992788424741`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0986892226410199`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030905006520719415`
- `max_f1`: `0.9465648854961832`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.29040321445650746`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
