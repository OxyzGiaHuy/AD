# Run ablation_alpha_0p75_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9615295420501094`
- `auroc`: `0.9239285714285714`
- `brier`: `0.22917021689562247`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04787389852783905`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018548728390173478`
- `max_f1`: `0.8923076923076924`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6502600120551846`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
