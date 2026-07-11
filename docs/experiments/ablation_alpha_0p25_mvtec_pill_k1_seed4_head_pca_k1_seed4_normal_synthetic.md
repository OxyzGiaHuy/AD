# Run ablation_alpha_0p25_mvtec_pill_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9490288186907909`
- `auroc`: `0.7577741407528642`
- `brier`: `0.21140747246181849`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2869258237456134`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002444061389315628`
- `max_f1`: `0.9155844155844156`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6155603729173853`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
