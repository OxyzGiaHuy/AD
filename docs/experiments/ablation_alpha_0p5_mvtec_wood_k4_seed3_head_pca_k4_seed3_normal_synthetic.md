# Run ablation_alpha_0p5_mvtec_wood_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9914891204859874`
- `auroc`: `0.9763157894736842`
- `brier`: `0.1883760770972718`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2514268386213085`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0054086008922585955`
- `max_f1`: `0.9747899159663865`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.566818666254332`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_wood_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
