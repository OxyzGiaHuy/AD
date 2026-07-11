# Run ablation_alpha_0p75_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.986677027050707`
- `auroc`: `0.9402618657937807`
- `brier`: `0.14544787731384073`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24937355054352814`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030057275009726337`
- `max_f1`: `0.9577464788732394`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4734708327514335`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
