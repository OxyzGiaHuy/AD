# Run ablation_alpha_0p25_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9950132283558398`
- `auroc`: `0.9823434991974318`
- `brier`: `0.2082760746172325`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3285158238349817`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001954372415048444`
- `max_f1`: `0.9772727272727273`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6093325458745678`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
