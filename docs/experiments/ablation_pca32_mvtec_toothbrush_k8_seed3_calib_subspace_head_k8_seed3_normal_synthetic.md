# Run ablation_pca32_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9871977906743796`
- `auroc`: `0.9666666666666667`
- `brier`: `0.153994105238167`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18406670611529125`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004516955332032272`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5781534116957425`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
