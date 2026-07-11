# Run ablation_pca32_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9798288232044233`
- `auroc`: `0.8966175668303328`
- `brier`: `0.1546487101741294`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1551380189592967`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014609047908804374`
- `max_f1`: `0.9355932203389831`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.543145001369536`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
