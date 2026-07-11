# Run ablation_pca64_mvtec_toothbrush_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.991118862718325`
- `auroc`: `0.9777777777777777`
- `brier`: `0.1671186189537761`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20366750515642618`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016965064707966078`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6139175227370609`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
