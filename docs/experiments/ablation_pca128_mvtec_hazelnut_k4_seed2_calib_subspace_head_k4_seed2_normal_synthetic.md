# Run ablation_pca128_mvtec_hazelnut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9760028457559802`
- `auroc`: `0.9567857142857142`
- `brier`: `0.3486090336899011`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3541422448375008`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025904587723992087`
- `max_f1`: `0.9210526315789473`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.2967375696548484`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
