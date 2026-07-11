# Run ablation_alpha_0p5_mvtec_wood_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_wood_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9846618111879303`
- `auroc`: `0.9578947368421052`
- `brier`: `0.19097651647979633`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25533637819410876`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029233670734529252`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.572418167406436`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_wood_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
