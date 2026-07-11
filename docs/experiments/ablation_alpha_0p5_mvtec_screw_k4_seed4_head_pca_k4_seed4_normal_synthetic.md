# Run ablation_alpha_0p5_mvtec_screw_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7886253472288514`
- `auroc`: `0.6081164172986268`
- `brier`: `0.20130970188029895`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15971655994653705`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023058033897541464`
- `max_f1`: `0.8689138576779026`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5937145626920379`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
