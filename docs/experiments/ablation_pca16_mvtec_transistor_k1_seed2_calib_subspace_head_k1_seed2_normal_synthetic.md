# Run ablation_pca16_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.6849067694684294`
- `auroc`: `0.7570833333333333`
- `brier`: `0.2225097444987877`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2161116574925836`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001990167200565338`
- `max_f1`: `0.6605504587155964`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7178295067143086`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
