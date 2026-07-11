# Run ablation_pca32_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.88621042018287`
- `auroc`: `0.8503571428571428`
- `brier`: `0.3611315741886265`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3620156548239968`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014112734828482974`
- `max_f1`: `0.8484848484848485`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.3061442902834504`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
