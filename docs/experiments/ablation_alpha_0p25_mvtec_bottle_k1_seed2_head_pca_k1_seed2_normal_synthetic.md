# Run ablation_alpha_0p25_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9691219336855653`
- `auroc`: `0.9111111111111111`
- `brier`: `0.22125672285856465`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24618823413389268`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017392879060233932`
- `max_f1`: `0.9264705882352942`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6353929309591931`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
