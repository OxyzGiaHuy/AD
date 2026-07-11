# Run head_pca_mvtec_tile_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9889391911580325`
- `auroc`: `0.974025974025974`
- `brier`: `0.25076356927989196`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.308413837200556`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016099182872945427`
- `max_f1`: `0.9651162790697675`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6946095125469132`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
