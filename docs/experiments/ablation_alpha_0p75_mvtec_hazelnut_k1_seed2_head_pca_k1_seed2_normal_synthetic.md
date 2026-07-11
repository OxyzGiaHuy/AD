# Run ablation_alpha_0p75_mvtec_hazelnut_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9117053245756995`
- `auroc`: `0.8692857142857143`
- `brier`: `0.231406473183761`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.03319718566807834`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024858723309907045`
- `max_f1`: `0.864516129032258`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6554466343257541`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
