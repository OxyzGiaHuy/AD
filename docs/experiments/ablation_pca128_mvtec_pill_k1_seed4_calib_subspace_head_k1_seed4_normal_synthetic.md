# Run ablation_pca128_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9757924458729915`
- `auroc`: `0.8873431533006001`
- `brier`: `0.15510177671829486`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15525719077287325`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021937356559102407`
- `max_f1`: `0.9440559440559441`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.1751958727911958`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
