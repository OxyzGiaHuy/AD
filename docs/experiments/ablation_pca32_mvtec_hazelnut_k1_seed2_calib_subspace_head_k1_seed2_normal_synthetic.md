# Run ablation_pca32_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8723604767863212`
- `auroc`: `0.775`
- `brier`: `0.363635882468483`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636360840363936`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013903198425065388`
- `max_f1`: `0.8098159509202454`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `6.289397403915431`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
