# Run ablation_pca128_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9873600183572198`
- `auroc`: `0.9496578690127078`
- `brier`: `0.18478619715900477`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18781752327214124`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024251412600278855`
- `max_f1`: `0.9518716577540107`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.2309379822362327`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
