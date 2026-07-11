# Run ablation_pca32_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9659126694749637`
- `auroc`: `0.9446428571428571`
- `brier`: `0.3011434058228049`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29793846390464085`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002379539575089108`
- `max_f1`: `0.9343065693430657`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.0252982249992828`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
