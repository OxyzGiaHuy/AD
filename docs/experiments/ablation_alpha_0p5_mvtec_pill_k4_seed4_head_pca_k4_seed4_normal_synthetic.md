# Run ablation_alpha_0p5_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9844606499096449`
- `auroc`: `0.9277141298417895`
- `brier`: `0.1775240024850628`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2848592778879725`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002593634705879017`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5453242845208819`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
