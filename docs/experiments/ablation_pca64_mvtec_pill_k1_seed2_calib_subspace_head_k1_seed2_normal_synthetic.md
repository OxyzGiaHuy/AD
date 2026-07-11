# Run ablation_pca64_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9862785245409285`
- `auroc`: `0.9318057828696127`
- `brier`: `0.15474353459083853`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15517529934466245`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002011442802355675`
- `max_f1`: `0.9494949494949495`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2361223072817278`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
