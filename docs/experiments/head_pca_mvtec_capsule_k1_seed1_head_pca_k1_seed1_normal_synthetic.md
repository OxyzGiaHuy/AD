# Run head_pca_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_capsule_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.835598471019911`
- `auroc`: `0.6094934184284004`
- `brier`: `0.24087961871310457`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31517802314324816`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016179538162594492`
- `max_f1`: `0.927038626609442`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6748937940963613`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
