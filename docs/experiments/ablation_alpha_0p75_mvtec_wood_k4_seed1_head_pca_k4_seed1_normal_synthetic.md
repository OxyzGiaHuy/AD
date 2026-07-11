# Run ablation_alpha_0p75_mvtec_wood_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9989159175039662`
- `auroc`: `0.9964912280701754`
- `brier`: `0.1790605931873553`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2613075073761275`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023890326530495777`
- `max_f1`: `0.9836065573770492`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5448829217297442`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
