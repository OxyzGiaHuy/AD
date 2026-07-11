# Run ablation_pca128_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9847770486916572`
- `auroc`: `0.9375340971085652`
- `brier`: `0.06051564418361036`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05689013318938048`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018726808916844295`
- `max_f1`: `0.958041958041958`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.24302003755014445`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
