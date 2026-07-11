# Run ablation_pca32_mvtec_metal_nut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.974674251712703`
- `auroc`: `0.907624633431085`
- `brier`: `0.10981771050928665`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12147504472700149`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026001769725395286`
- `max_f1`: `0.9430051813471503`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.1593275477970464`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
