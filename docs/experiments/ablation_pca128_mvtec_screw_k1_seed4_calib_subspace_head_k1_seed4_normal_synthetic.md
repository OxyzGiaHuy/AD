# Run ablation_pca128_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7568739513902915`
- `auroc`: `0.5632301701168272`
- `brier`: `0.2559618027041214`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2559124186635017`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019243471324443817`
- `max_f1`: `0.8561151079136691`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.9578081319873255`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
