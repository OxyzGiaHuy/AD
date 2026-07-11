# Run ablation_alpha_0p5_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9867592878251831`
- `auroc`: `0.9399890889252591`
- `brier`: `0.16616253257437796`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2824068333574397`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002616620438541481`
- `max_f1`: `0.9611307420494699`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.521005128038014`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
