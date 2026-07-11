# Run ablation_pca16_mvtec_capsule_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9280955048496573`
- `auroc`: `0.7403270841643399`
- `brier`: `0.33374129013218456`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3679431632727526`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017502208832990038`
- `max_f1`: `0.911504424778761`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.6251760829947968`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
