# Run head_pca_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9662191927438469`
- `auroc`: `0.8747506980454727`
- `brier`: `0.23728292931989922`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3173560978788319`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015752401739133127`
- `max_f1`: `0.9422222222222222`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6676708040771627`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
