# Run ablation_pca16_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.986116200163153`
- `auroc`: `0.9653679653679653`
- `brier`: `0.2792885133234737`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2784846919214624`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015898987045909604`
- `max_f1`: `0.9418604651162791`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.9374055271128703`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
