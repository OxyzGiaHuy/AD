# Run ablation_pca128_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9606892032548449`
- `auroc`: `0.9278571428571428`
- `brier`: `0.3636137021068405`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636247255585411`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0031683846630833367`
- `max_f1`: `0.8843537414965986`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `4.49007000725967`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
