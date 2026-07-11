# Run ablation_pca64_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.991118862718325`
- `auroc`: `0.9777777777777777`
- `brier`: `0.12831443898696665`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1743267568803969`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004636957709278379`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.48957016284474986`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
