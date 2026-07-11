# Run ablation_pca16_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9480374380391963`
- `auroc`: `0.9047619047619048`
- `brier`: `0.2613141620339872`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3118185843310882`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0031949351261179133`
- `max_f1`: `0.9465648854961832`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.1189339455357667`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
