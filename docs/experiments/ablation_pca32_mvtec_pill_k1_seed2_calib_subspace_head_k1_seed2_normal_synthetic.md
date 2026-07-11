# Run ablation_pca32_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.982656929508578`
- `auroc`: `0.9132569558101473`
- `brier`: `0.1495157681541727`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15075927642648085`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00205661779169194`
- `max_f1`: `0.9366197183098591`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.99285109796838`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
