# Run ablation_pca64_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9760975195126059`
- `auroc`: `0.9564285714285714`
- `brier`: `0.36363145560595495`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636338889598847`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021796238693324002`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `5.067884249936092`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
