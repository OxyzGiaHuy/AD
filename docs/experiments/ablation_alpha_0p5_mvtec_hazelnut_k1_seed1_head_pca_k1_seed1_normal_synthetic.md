# Run ablation_alpha_0p5_mvtec_hazelnut_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9505142759064723`
- `auroc`: `0.8932142857142857`
- `brier`: `0.22773237866119445`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07722314271059903`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002762779373336922`
- `max_f1`: `0.8805970149253731`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6477738225649533`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
