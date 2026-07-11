# Run ablation_pca128_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9901334079747146`
- `auroc`: `0.9821428571428571`
- `brier`: `0.34218326876916594`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3521894352002578`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015565872869708322`
- `max_f1`: `0.9459459459459459`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.8742648604793442`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
