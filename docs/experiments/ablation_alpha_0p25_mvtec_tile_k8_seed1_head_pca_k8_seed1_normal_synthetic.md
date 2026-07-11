# Run ablation_alpha_0p25_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9882367794346647`
- `auroc`: `0.9704184704184704`
- `brier`: `0.22063665244780067`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2936289697630793`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024320313500033486`
- `max_f1`: `0.9707602339181286`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6342687343982131`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
