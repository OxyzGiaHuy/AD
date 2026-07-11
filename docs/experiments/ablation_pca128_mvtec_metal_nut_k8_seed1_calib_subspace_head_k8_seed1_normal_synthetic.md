# Run ablation_pca128_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9987802541383524`
- `auroc`: `0.9946236559139785`
- `brier`: `0.07104026753261529`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08619353048827336`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003503252031362575`
- `max_f1`: `0.9837837837837838`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.24345589079639895`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
