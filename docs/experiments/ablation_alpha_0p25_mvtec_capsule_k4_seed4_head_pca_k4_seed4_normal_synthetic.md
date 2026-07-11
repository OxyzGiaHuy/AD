# Run ablation_alpha_0p25_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9691074630453537`
- `auroc`: `0.8651775029916234`
- `brier`: `0.2011160257618188`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25724092893528216`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024507912581391406`
- `max_f1`: `0.9145299145299145`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5944584082601244`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
