# Run ablation_alpha_0p75_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9728187079221484`
- `auroc`: `0.9457142857142857`
- `brier`: `0.22792028366817405`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06250305067409168`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003934474594213746`
- `max_f1`: `0.9323308270676691`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6471598023953564`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
