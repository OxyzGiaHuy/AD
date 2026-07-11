# Run ablation_alpha_0p75_mvtec_zipper_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.979219161700794`
- `auroc`: `0.930672268907563`
- `brier`: `0.16951723069498129`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2683838708511251`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002080214438059472`
- `max_f1`: `0.9543568464730291`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5252562535925338`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
