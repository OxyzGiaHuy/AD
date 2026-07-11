# Run ablation_alpha_0p5_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9826789125463636`
- `auroc`: `0.9211674849972722`
- `brier`: `0.17788310761467288`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29672395219346004`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004342930246434526`
- `max_f1`: `0.9469964664310954`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5463010691697102`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
