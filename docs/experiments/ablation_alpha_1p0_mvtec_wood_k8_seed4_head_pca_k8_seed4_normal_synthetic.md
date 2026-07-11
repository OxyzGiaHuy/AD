# Run ablation_alpha_1p0_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9747311649926511`
- `auroc`: `0.9649122807017544`
- `brier`: `0.17898134665426446`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2451127888281134`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003100538036868542`
- `max_f1`: `0.9917355371900827`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5428056792297736`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
