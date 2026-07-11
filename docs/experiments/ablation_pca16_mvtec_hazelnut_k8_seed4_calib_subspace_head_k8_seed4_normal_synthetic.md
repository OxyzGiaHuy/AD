# Run ablation_pca16_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8998256235910975`
- `auroc`: `0.8414285714285714`
- `brier`: `0.27560421913370164`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29418753900311206`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026259480382908474`
- `max_f1`: `0.8536585365853658`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.0306734840441034`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
