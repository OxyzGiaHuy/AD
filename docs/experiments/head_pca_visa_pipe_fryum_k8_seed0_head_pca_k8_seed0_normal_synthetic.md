# Run head_pca_visa_pipe_fryum_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pipe_fryum_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9760410612389907`
- `auroc`: `0.9504`
- `brier`: `0.23586484473631222`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26034788548946386`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003248891830444336`
- `max_f1`: `0.9178743961352657`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6648424449511219`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pipe_fryum_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
