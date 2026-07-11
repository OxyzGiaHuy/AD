# Run ablation_pca64_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7700436054666121`
- `auroc`: `0.815`
- `brier`: `0.5923272250119376`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5957400816679`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015131216123700142`
- `max_f1`: `0.7216494845360825`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.17078969716993`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
