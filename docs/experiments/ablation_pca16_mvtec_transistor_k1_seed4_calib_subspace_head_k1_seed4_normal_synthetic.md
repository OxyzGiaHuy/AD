# Run ablation_pca16_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7224817828739507`
- `auroc`: `0.7883333333333333`
- `brier`: `0.21451626002604493`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17279787171632052`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001425633393228054`
- `max_f1`: `0.6818181818181818`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7497040394432056`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
