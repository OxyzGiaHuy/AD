# Run ablation_pca128_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9916967658437018`
- `auroc`: `0.9736842105263158`
- `brier`: `0.17683673390541074`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2002978977523273`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002910105511546135`
- `max_f1`: `0.9661016949152542`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.098485842532178`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
