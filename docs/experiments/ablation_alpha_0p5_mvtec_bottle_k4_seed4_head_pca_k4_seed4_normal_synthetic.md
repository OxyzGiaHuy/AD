# Run ablation_alpha_0p5_mvtec_bottle_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9933833625413064`
- `auroc`: `0.9777777777777777`
- `brier`: `0.19213459488118345`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34699155192777337`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003087286556880158`
- `max_f1`: `0.9538461538461539`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.575085696481444`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
