# Run ablation_alpha_0p5_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9821354657739444`
- `auroc`: `0.9657142857142857`
- `brier`: `0.22112761796836589`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.052179609103636226`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002998748607933521`
- `max_f1`: `0.950354609929078`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6336101605115091`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
