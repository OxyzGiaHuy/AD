# Run ablation_pca16_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9734413995589437`
- `auroc`: `0.9303751803751804`
- `brier`: `0.21145895858247588`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16636166638798183`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014687025935476662`
- `max_f1`: `0.9156626506024096`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.679856653269797`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
