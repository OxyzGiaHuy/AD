# Run ablation_alpha_0p5_mvtec_screw_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.906605305399499`
- `auroc`: `0.7710596433695429`
- `brier`: `0.2039614009552131`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14857738576829438`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002015792392194271`
- `max_f1`: `0.8582089552238806`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5993867780916066`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
