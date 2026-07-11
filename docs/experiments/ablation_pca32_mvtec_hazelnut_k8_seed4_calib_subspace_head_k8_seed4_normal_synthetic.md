# Run ablation_pca32_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9701792710998662`
- `auroc`: `0.9628571428571429`
- `brier`: `0.2620661054474881`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2868061596019701`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002828653326088732`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.2939801138821743`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
