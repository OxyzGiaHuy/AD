# Run ablation_pca16_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9693401614003916`
- `auroc`: `0.8513366066557556`
- `brier`: `0.10058320139850101`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.107882828939139`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018448177613541038`
- `max_f1`: `0.9423728813559322`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.1248019491265304`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
