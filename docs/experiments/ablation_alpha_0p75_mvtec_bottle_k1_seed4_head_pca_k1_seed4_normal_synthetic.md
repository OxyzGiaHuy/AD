# Run ablation_alpha_0p75_mvtec_bottle_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_bottle_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9865671138423576`
- `auroc`: `0.9547619047619048`
- `brier`: `0.18500655248410064`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21132072339574975`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002342893910336207`
- `max_f1`: `0.9457364341085271`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5580718365371317`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_bottle_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
