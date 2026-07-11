# Run ablation_pca32_mvtec_hazelnut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9948104335752496`
- `auroc`: `0.9917857142857143`
- `brier`: `0.15715700883600692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21701404276219283`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003021912310611118`
- `max_f1`: `0.9790209790209791`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.47207617560446685`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
