# Run ablation_alpha_0p5_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8845280336412445`
- `auroc`: `0.7362164377946301`
- `brier`: `0.19873963714332732`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14388154931366445`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028798936633393168`
- `max_f1`: `0.8561151079136691`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5881501326474736`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
