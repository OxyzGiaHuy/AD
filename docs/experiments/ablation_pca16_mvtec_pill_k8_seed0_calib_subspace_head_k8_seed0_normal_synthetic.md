# Run ablation_pca16_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.962373792909356`
- `auroc`: `0.82924168030551`
- `brier`: `0.09003076014990358`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06435347830843242`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0037027274866304`
- `max_f1`: `0.9459459459459459`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.31261098429542333`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
