# Run ablation_alpha_0p5_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.970735298683075`
- `auroc`: `0.9425`
- `brier`: `0.22434584246820227`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04545178575949227`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002462309937585484`
- `max_f1`: `0.920863309352518`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6404840099320894`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
