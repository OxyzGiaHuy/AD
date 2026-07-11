# Run ablation_alpha_0p5_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9809340403246656`
- `auroc`: `0.9080741953082379`
- `brier`: `0.1799834027345457`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2257100061742131`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004443007515754528`
- `max_f1`: `0.9494949494949495`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.550474944993013`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
