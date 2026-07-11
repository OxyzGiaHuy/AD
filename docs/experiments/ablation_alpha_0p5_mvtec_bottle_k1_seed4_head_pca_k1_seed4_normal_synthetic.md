# Run ablation_alpha_0p5_mvtec_bottle_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.984035253274394`
- `auroc`: `0.9484126984126984`
- `brier`: `0.19627232918962834`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22221266648855553`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001930725143616458`
- `max_f1`: `0.9457364341085271`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5834643904492814`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
