# Run ablation_pca32_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9881595026600999`
- `auroc`: `0.9789285714285715`
- `brier`: `0.3636349678449415`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636356657201594`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026131583377718925`
- `max_f1`: `0.9395973154362416`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `6.1736856143133965`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
