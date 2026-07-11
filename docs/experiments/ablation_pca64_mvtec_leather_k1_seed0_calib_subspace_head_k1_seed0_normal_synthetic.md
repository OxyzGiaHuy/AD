# Run ablation_pca64_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_leather_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9983155233823904`
- `auroc`: `0.9952445652173914`
- `brier`: `0.251210771266124`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25450034487632023`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014321797287031527`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.4140157688111326`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
