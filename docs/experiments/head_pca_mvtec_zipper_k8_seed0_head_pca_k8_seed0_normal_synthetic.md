# Run head_pca_mvtec_zipper_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.986443079455903`
- `auroc`: `0.9516806722689075`
- `brier`: `0.24682422882587923`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3243177925908802`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015456878290271128`
- `max_f1`: `0.9512195121951219`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6866484878699723`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_zipper_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
