# Run ablation_pca32_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9853724354337358`
- `auroc`: `0.956140350877193`
- `brier`: `0.24044910429453467`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2404777060581158`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024749891054403933`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.3919903426804243`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
