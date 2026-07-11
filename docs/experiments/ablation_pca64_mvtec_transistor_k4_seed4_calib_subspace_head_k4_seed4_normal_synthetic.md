# Run ablation_pca64_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8984865376508839`
- `auroc`: `0.9220833333333334`
- `brier`: `0.2543166217928135`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.304797180229798`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002846834007650614`
- `max_f1`: `0.8354430379746836`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.0230172746178057`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
