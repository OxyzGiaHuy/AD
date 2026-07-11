# Run ablation_pca16_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9844036284674621`
- `auroc`: `0.9517543859649122`
- `brier`: `0.24050540865386505`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2405058688755276`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014757998523455631`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `4.326510471860359`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
