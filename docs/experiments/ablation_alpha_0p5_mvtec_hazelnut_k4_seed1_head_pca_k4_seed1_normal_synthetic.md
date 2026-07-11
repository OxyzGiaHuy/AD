# Run ablation_alpha_0p5_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9615011795169585`
- `auroc`: `0.9221428571428572`
- `brier`: `0.22517137979837215`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.028995506871830317`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002460019561377439`
- `max_f1`: `0.8872180451127819`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.642281132145314`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
