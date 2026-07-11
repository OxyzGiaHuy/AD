# Run ablation_pca128_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.883671701207463`
- `auroc`: `0.9079166666666667`
- `brier`: `0.3681768461740987`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4311211857199668`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016326295770704745`
- `max_f1`: `0.8095238095238095`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.5376150412745366`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
