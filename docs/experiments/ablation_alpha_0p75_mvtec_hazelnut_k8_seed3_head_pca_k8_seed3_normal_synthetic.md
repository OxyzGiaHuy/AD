# Run ablation_alpha_0p75_mvtec_hazelnut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9843797864794956`
- `auroc`: `0.9710714285714286`
- `brier`: `0.2270699482323531`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.051669580286199404`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002507991868663918`
- `max_f1`: `0.9577464788732394`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6453669446880772`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
