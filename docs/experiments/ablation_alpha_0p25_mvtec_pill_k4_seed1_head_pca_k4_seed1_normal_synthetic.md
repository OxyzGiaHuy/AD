# Run ablation_alpha_0p25_mvtec_pill_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9858742215331683`
- `auroc`: `0.933442444080742`
- `brier`: `0.2018518950240998`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32969301653479394`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003208464245774789`
- `max_f1`: `0.9469964664310954`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5961421404202103`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
