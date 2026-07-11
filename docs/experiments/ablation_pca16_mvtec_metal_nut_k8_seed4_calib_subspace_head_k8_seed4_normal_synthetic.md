# Run ablation_pca16_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9247904212362239`
- `auroc`: `0.7873900293255132`
- `brier`: `0.10265907859471918`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.105641360807678`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026987629416196242`
- `max_f1`: `0.9292929292929293`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4190349413088312`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
