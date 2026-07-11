# Run ablation_alpha_0p75_mvtec_transistor_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8028513652382845`
- `auroc`: `0.855`
- `brier`: `0.3064218544802384`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2720612144470215`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004248143211007118`
- `max_f1`: `0.7640449438202247`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8111055721996902`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
