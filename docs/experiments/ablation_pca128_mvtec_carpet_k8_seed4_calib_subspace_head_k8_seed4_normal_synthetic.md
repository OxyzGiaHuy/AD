# Run ablation_pca128_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9995167331158632`
- `auroc`: `0.9983948635634029`
- `brier`: `0.04794316090886676`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07736119838893163`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026161758404256953`
- `max_f1`: `0.9943502824858758`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.14440446023370185`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
