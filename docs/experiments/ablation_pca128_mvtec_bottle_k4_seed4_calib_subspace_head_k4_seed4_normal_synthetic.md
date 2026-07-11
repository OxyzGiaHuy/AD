# Run ablation_pca128_mvtec_bottle_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9978001338224538`
- `auroc`: `0.9928571428571429`
- `brier`: `0.18685937894152516`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2029745998870896`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016409971538078353`
- `max_f1`: `0.9841269841269841`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8470534555936353`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
