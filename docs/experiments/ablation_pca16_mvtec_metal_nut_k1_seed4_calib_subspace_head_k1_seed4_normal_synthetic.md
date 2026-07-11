# Run ablation_pca16_mvtec_metal_nut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9309545599510848`
- `auroc`: `0.7961876832844574`
- `brier`: `0.17297216008225644`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13945030647775403`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037001402481742526`
- `max_f1`: `0.9238578680203046`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6011141482288095`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
