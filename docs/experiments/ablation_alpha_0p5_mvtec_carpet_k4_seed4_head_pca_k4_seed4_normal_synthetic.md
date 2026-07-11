# Run ablation_alpha_0p5_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.986060478010954`
- `auroc`: `0.949438202247191`
- `brier`: `0.17878242049260354`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.313764257563485`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002352886061128388`
- `max_f1`: `0.9418604651162791`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5474803952600501`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
