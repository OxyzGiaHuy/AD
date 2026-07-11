# Run head_pca_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9870421261278943`
- `auroc`: `0.9429896344789962`
- `brier`: `0.24798600389155706`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4032015936103409`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015834520520742782`
- `max_f1`: `0.9605734767025089`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6890916321460331`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
