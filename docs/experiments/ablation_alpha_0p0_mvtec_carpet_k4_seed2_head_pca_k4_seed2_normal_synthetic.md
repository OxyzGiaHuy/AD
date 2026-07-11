# Run ablation_alpha_0p0_mvtec_carpet_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_carpet_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9990107006884094`
- `auroc`: `0.9967897271268058`
- `brier`: `0.24914158838277348`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.44505224217716444`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003568657841055821`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6908541636234772`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_carpet_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
