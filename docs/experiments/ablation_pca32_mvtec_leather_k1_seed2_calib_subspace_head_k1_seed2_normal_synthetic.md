# Run ablation_pca32_mvtec_leather_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_leather_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9974177420965502`
- `auroc`: `0.9925271739130435`
- `brier`: `0.2124865434843527`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22595608240414045`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00222247822450534`
- `max_f1`: `0.9735449735449735`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.0642379376516793`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_leather_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
