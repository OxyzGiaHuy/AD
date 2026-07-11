# Run ablation_alpha_0p75_mvtec_grid_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.999097505881862`
- `auroc`: `0.9974937343358395`
- `brier`: `0.186931376530423`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23117094849928832`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00208008883950802`
- `max_f1`: `0.9827586206896551`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5610094286296576`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
