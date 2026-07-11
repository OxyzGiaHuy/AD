# Run ablation_pca128_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7911871316849759`
- `auroc`: `0.8245833333333333`
- `brier`: `0.5919401506181019`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.595633100271225`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001757305096834898`
- `max_f1`: `0.6987951807228916`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `4.107914045913237`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
