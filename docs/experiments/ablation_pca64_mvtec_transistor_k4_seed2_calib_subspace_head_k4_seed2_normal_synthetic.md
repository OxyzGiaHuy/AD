# Run ablation_pca64_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.852016736956287`
- `auroc`: `0.8870833333333333`
- `brier`: `0.3428700659984362`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38152128193876705`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002440588492900133`
- `max_f1`: `0.7848101265822784`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.80013304673167`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
